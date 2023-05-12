from conans import ConanFile, Meson
import os

class RangConan(ConanFile):
    generators = "pkg_config"
    exports_sources = "*"

    def build(self):
        meson = Meson(self)
        meson.configure()
        meson.build()

    def imports(self):
        self.copy("*.hpp")

    def test(self):
        self.run(f".{os.sep}visualTest")
