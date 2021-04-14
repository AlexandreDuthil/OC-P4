#! /usr/bin/env python3
# coding: utf-8

import Controller.main as controller


def main():
    while controller.Tournament.play:
        controller.Tournament.menu()


if __name__ == "__main__":
    main()