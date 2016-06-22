# Documentation: https://github.com/Homebrew/brew/blob/master/share/doc/homebrew/Formula-Cookbook.md
#                http://www.rubydoc.info/github/Homebrew/brew/master/Formula

class HomebrewCmd < Formula
  desc ""
  homepage ""
  url "https://github.com/cundohubs/homebrew-cmd/archive/0.0.3.tar.gz"
  version "0.0.3"
  sha256 "fe40a2ef2568c996ed8d6d5ac6543547d96a7ff67152a13a435db70f406fce89"


  def install
    # ENV.deparallelize  # if your formula fails when building in parallel
    bin.install "curalate"
  end

end
