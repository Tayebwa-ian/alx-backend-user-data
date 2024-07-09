#!/usr/bin/env python3
"""
Authentication Module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class implementation"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Later implementation
        """
        if not path or not excluded_paths:
            return True
        if len(excluded_paths) < 1:
            return True
        for p in excluded_paths:
            if self.strip_slash(p) == self.strip_slash(path):
                return False
        return True

    @staticmethod
    def strip_slash(data: str) -> str:
        """
        Remove a forward slash character at the end of the string
        Arg:
         data: the string to check and strip
        """
        if data.endswith("/"):
            return data[:-1]
        return data

    def authorization_header(self, request=None) -> str:
        """
        recieves request and retrrives header information
        Arg:
            request: Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns current user if exists
        Arg:
            request: Flask request object
        """
        return None
