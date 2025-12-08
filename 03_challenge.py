def is_palindrome(text: str) -> bool:
    text_revers = text[::-1]
    if text == text_revers:
        return True
    else:
        return False
    
print(is_palindrome("mada"))