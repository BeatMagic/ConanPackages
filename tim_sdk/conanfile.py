import os.path

import copy
import shutil
import subprocess
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

    exports_sources = "./*"

    def source(self):
        if self.settings.os == "Windows":
            # https://im.sdk.cloud.tencent.cn/download/plus/6.1.2155/ImSDK_Windows_CPP_6.1.2155.zip
            tools.download("https://im.sdk.cloud.tencent.cn/download/plus/6.1.2155/ImSDK_Windows_CPP_6.1.2155.zip",
                           "ImSDK_Windows_CPP.zip", verify=False)

            tools.unzip("ImSDK_Windows_CPP.zip", ".")
        elif self.settings.os == "Macos":
            # https://im.sdk.cloud.tencent.cn/download/plus/6.1.2155/cross_platform/ImSDK_Mac_CPP_6.1.2155.framework.zip
            tools.download("https://im.sdk.cloud.tencent.cn/download/plus/6.1.2155/cross_platform/ImSDK_Mac_CPP_6.1.2155.framework.zip",
                           "ImSDKForMac_CPP.framework.zip", verify=False)
            tools.unzip("ImSDKForMac_CPP.framework.zip", ".")
            os.chdir("ImSDKForMac_CPP.framework")
            os.unlink("Headers")
            os.unlink("ImSDKForMac_CPP")
            os.unlink("Modules")
            os.unlink("Resources")
            os.unlink("Versions/Current")

            # tools.download("https://sdk-im-1252463788.cos.ap-hongkong.myqcloud.com/download/plus/6.1.2155/ImSDKForMac_Plus_6.1.2155.framework.zip",
            #                "ImSDKForMac_Plus.framework.zip", verify=False)
            # tools.unzip("ImSDKForMac_Plus.framework.zip", ".")

            # tools.download("https://im.sdk.cloud.tencent.cn/download/plus/6.1.2155/cross_platform/ImSDK_iOS_CPP_6.1.2155.framework.zip",
            #                "ImSDK_CPP.framework.zip", verify=False)
            # tools.unzip("ImSDK_CPP.framework.zip", ".")

    # def config_options(self):
    #     if self.settings.os == "Windows":
    #         del self.options.fPIC

    # def build(self):
    #     cmake = CMake(self)
    #     cmake.configure(source_folder="src")
    #     cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)
    # def build(self):
    #     shutil.copyfile(os.path.join(self.source_folder, "ImSDK_Mac_CPP.framework"),
    #                     os.path.join(self.build_folder, "ImSDK_Mac_CPP.framework"))

    def package(self):
        # self.copy("*.h", dst="include", src="src")
        # self.copy("*.lib", dst="lib", keep_path=False)
        # self.copy("*.dll", dst="bin", keep_path=False)
        # self.copy("*.dylib*", dst="lib", keep_path=False)
        # self.copy("*.so", dst="lib", keep_path=False)
        # self.copy("*.a", dst="lib", keep_path=False)
        if self.settings.os == "Macos":
            # 复制头文件
            self.copy("*.h", dst="include", src="ImSDKForMac_CPP.framework/Versions/A/Headers")
            # 将ImSDKFormac_CPP.framework复制到lib/目录
            tools.mkdir("ImSDKForMac_CPP.framework")
            self.copy("*", dst="ImSDKForMac_CPP.framework", src="ImSDKForMac_CPP.framework")


    def package_info(self):
        if self.settings.os == "Macos":
            # self.cpp_info.libs = ["ImSDKForMac_CPP"]
            self.cpp_info.frameworkdirs.append(self.package_folder)
            self.cpp_info.frameworks.append("ImSDKForMac_CPP")

            # if tools.is_apple_os(self.settings.os):
            #     self.cpp_info.frameworks.extend([
            #                                  "Cocoa",
            #                                  "Accelerate",
            #                                  "Foundation",
            #                                  "QuartzCore",
            #                                  "CoreMedia",
            #                                  "CoreMIDI",
            #                                  "CoreAudioKit",
            #                                  "Carbon",
            #                                  "CoreFoundation",
            #                                  "IOKit",
            #                                  "AppKit"])

        # self.cpp_info.exelinkflags.append("-framework ImSDKForMac_CPP")
        # self.cpp_info.sharedlinkflags = self.cpp_info.exelinkflags
        # # self.cpp_info.libs = ["TimSdk"]
        # # if self.settings.os == "Macos":
        # #     frameworks = ["ImSDKForMac_CPP"]
        # #
        # #     for framework in frameworks:
        # #         self.cpp_info.exelinkflags.append("-framework %s" % framework)
