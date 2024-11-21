import re


token_specification_with_single_quote_string = [
    ('ID',       r'[a-zA-Z_]\w*'), 
    ('NUMBER',   r'\d+\.\d+|\d+'),  # 浮点数或整数
    ('ASSIGN',   r'='),             
    ('END',      r';'),             
    ('SKIP',     r'[ \t]+'),        
    ('NEWLINE',  r'\n'),            
    ('LBRACE',   r'\{'),            
    ('RBRACE',   r'\}'),            
    ('LPAREN',   r'$'),            
    ('RPAREN',   r'$'),            
    ('DOT',      r'\.'),            
    ('STRING',   r'"[^"]*"'),       
    ('SINGLE_QUOTE_STRING', r"'[^']*'"),  # 单引号字符串字面量
    ('GREATER_SINGLE_QUOTE', r'>\''),
    ('LESS_THAN', r'<'),            
    ('SLASH',    r'/'),             # 匹配斜杠
    ('BACKSLASH', r'\\\\'),         # 匹配反斜杠，注意需要转义
    ('MISMATCH', r'.')              
]

# 建立包含新正则表达式的完整匹配规则
token_regex_with_single_quote_string = '|'.join('(?P<%s>%s)' % pair for pair in token_specification_with_single_quote_string)

# 创建词法分析器
def lexer_with_single_quote_string(code):
    pos = 0
    while pos < len(code):
        match = re.match(token_regex_with_single_quote_string, code[pos:])
        if match is not None:
            type = match.lastgroup
            value = match.group(type)
            if type == 'SKIP':
                pass
            elif type == 'NEWLINE':
                pass
            elif type == 'MISMATCH':
                raise RuntimeError(f'Unexpected character {value}')
            else:
                yield type, value
            pos += match.end()
        else:
            yield "error", "error"
