#! /usr/bin/env python3
# coding: utf-8

from controller.menu import Menu


def main():
    main_menu = Menu()
    while Menu.play:
        main_menu.display()


if __name__ == "__main__":
    main()
