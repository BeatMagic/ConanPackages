import os.path
from conans import ConanFile, CMake, tools


class TimSdkConan(ConanFile):
    name = "TimSdk"
    version = "6.1.2"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of TimSdk here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    exports_sources = "src/*"

    def source(self):
        if self.settings.os == "Windows":
            # https://im.sdk.cloud.tencent.cn/download/plus/6.1.2155/ImSDK_Windows_CPP_6.1.2155.zip
            tools.download("https://im.sdk.cloud.tencent.cn/download/plus/6.1.2155/ImSDK_Windows_CPP_6.1.2155.zip",
                           "ImSDK_Windows_CPP.zip", verify=False)

            tools.unzip("ImSDK_Windows_CPP.zip", ".")
        # elif self.settings.os == "Macos":
        #     # https://im.sdk.cloud.tencent.cn/download/plus/6.1.2155/cross_platform/ImSDK_Mac_CPP_6.1.2155.framework.zip
        #     tools.download("https://im.sdk.cloud.tencent.cn/download/plus/6.1.2155/cross_platform/ImSDK_Mac_CPP_6.1.2155.framework.zip",
        #                    "ImSDKForMac_CPP.framework.zip", verify=False)
        #     tools.unzip("ImSDKForMac_CPP.framework.zip", ".")

    def package(self):
        if self.settings.os == "Macos":
            # 复制头文件
            self.copy("*.h", dst="include", src="src/ImSDKForMac_CPP.framework/Versions/A/Headers")
            # 将ImSDKFormac_CPP.framework复制到lib/目录
            tools.mkdir("lib/ImSDKForMac_CPP.framework")
            self.copy("*", dst="lib/ImSDKForMac_CPP.framework", src="src/ImSDKForMac_CPP.framework")
        elif self.settings.os == "Windows":
            self.copy("*.h", dst="include", src="ImSDK_Windows_CPP/include")
            self.copy("*.lib", dst="lib", src="ImSDK_Windows_CPP/lib/Win64", keep_path=False)
            self.copy("*.dll", dst="bin", src="ImSDK_Windows_CPP/lib/Win64", keep_path=False)
            

    def package_info(self):
        if self.settings.os == "Macos":
            self.cpp_info.frameworkdirs.append(os.path.join(self.package_folder, 'lib'))
            self.cpp_info.frameworks.append("ImSDKForMac_CPP")
        elif self.settings.os == "Windows":
            self.cpp_info.libs = ["ImSDK"]
