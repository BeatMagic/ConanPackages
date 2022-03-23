import subprocess
from conans import ConanFile, CMake, tools


class AliyunOssConan(ConanFile):
    name = "AliyunOss"
    version = "1.9.0"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of AliyunOss here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    generators = "cmake"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    requires = ["openssl/1.1.1l", "libcurl/7.80.0"]

    def source(self):
        git = tools.Git(folder="src")
        git.clone('https://github.com/aliyun/aliyun-oss-cpp-sdk.git', 'master')
        subprocess.check_call(
            ['git', 'checkout', '--quiet', 'bf4a2d7c97ed1a2c6fe277b3163f53d7d249bf7a'], cwd="src")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_SAMPLE'] = 'OFF'
        cmake.configure()
        cmake.build()

    def package(self):
        # cmake = CMake(self)
        # cmake.install()
        self.copy("*.h", dst="include", src="src/sdk/include")

        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["alibabacloud-oss-cpp-sdk"]
