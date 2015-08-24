# Learn Go

https://gobyexample.com/

## Install
I'm using Ubuntu 14 Trust Tahr. Download the necessary package for your OS.

Find the latest download link @ https://golang.org/dl/

    wget https://storage.googleapis.com/golang/go1.4.linux-amd64.tar.gz
    tar -C /usr/local -xzf go*.tar.gz
    export PATH=$PATH:/usr/local/go/bin

## Using Go

See commands

    go

Run a `.go` file

    go run <file>

Compile a `.go` file

    go build <file>

## Language

The following `:=` auto detects a type:

    x := "blah"

What does `_` mean? in the following example:

    _, test := "hi"

