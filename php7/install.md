# Install PHP7 Release Candidate X

The easiest way is to install with BitNami or a PPA.
I personally use a clone VM in Linux to and uninstalled PHP5 and just used the
PPA. Otherwise you can look at how to compile it yourself if you want.

## Ubuntu PPA

Visit: https://launchpad.net/~ondrej/+archive/ubuntu/php-7.0

    sudo apt-add-repository ppa:ondrej/php-7.0
    sudo apt-get update
    # sudo apt-get remove php5  # If you are doing this.
    sudo apt-get install php7.0


## Ubuntu Build

This Gist will help you get started.

Visit: https://gist.github.com/JREAM/6c69e4891ebf01484bec

## Windows

Visit: https://bitnami.com/stack/wamp/installer
