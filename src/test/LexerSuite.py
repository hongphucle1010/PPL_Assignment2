import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # !-------------------Test Keywords 3.3.1-------------------!
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_lower_upper_id(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 102))

    def test_identifier(self):
        """test identifiers with wrong identifier name"""
        self.assertTrue(TestLexer.checkLexeme("123abc", "123,abc,<EOF>", 103))

    def test_identifier_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc123", "abc123,<EOF>", 104))

    def test_identifier_3(self):
        """test identifiers length"""
        self.assertTrue(TestLexer.checkLexeme("a b c", "a,b,c,<EOF>", 105))

    def test_invalid_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("aA_b?C", "aA_b,ErrorToken ?", 106))

    def test_invalid_identifier_2(self):
        """test identifiers with hyphen"""
        self.assertTrue(TestLexer.checkLexeme("a-b-c", "a,-,b,-,c,<EOF>", 107))

    # !-------------------Test Keywords 3.3.2-------------------!
    def test_keyword(self):
        """test keywords if, else, for, return"""
        self.assertTrue(
            TestLexer.checkLexeme("if else for return", "if,else,for,return,<EOF>", 108)
        )

    def test_keyword_2(self):
        """test keyword, func, type, struct, interface, string, int, float, boolean"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "func type struct interface string int float boolean",
                "func,type,struct,interface,string,int,float,boolean,<EOF>",
                109,
            )
        )

    def test_keyword_3(self):
        """test keywords const, var, continue, break, range, nil, true, false"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "const var continue break range nil true false",
                "const,var,continue,break,range,nil,true,false,<EOF>",
                110,
            )
        )

    def test_wrong_keyword(self):
        """test wrong keyword"""
        self.assertTrue(TestLexer.checkLexeme("ifelse", "ifelse,<EOF>", 111))

    def test_wrong_keyword_2(self):
        """test wrong keyword"""
        self.assertTrue(TestLexer.checkLexeme("fori = 2", "fori,=,2,<EOF>", 112))

    # !-------------------Test operators 3.3.3-------------------!
    def test_operator(self):
        """test operators"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "+ - * / % && || ! == != < > <= >= = := += -= *= /= %= .",
                "+,-,*,/,%,&&,||,!,==,!=,<,>,<=,>=,=,:=,+=,-=,*=,/=,%=,.,<EOF>",
                113,
            )
        )

    def test_operator_2(self):
        """test operators that attached together"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "+-*/%&&||!===!=<><=>=:=+=-=*/=%=.",
                "+,-,*,/,%,&&,||,!=,==,!=,<,>,<=,>=,:=,+=,-=,*,/=,%=,.,<EOF>",
                114,
            )
        )

    def test_operator_3(self):
        """test operators that attached with numbers and identifiers"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "+-*/%&&||!===!=<>123abc>=:=+=-=*/=%=.",
                "+,-,*,/,%,&&,||,!=,==,!=,<,>,123,abc,>=,:=,+=,-=,*,/=,%=,.,<EOF>",
                115,
            )
        )

    # !-------------------Test Separators 3.3.4-------------------!
    # Separators: ( ) [ ] { } , ;
    def test_separator(self):
        """test separators"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "( ) [ ] { } , ;",
                "(,),[,],{,},,,;,<EOF>",
                116,
            )
        )

    def test_separator_2(self):
        """test separators that attached together"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "()[],{}",
                "(,),[,],,,{,},<EOF>",
                117,
            )
        )

    def test_separator_3(self):
        """test separators that attached with numbers and identifiers"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "()[],{}(12)(3{ab,c;})",
                "(,),[,],,,{,},(,12,),(,3,{,ab,,,c,;,},),<EOF>",
                118,
            )
        )

    # !-------------------Test Literals 3.3.5-------------------!
    # Literals: Integer, Float, String, Rune

    # Integer
    def test_decimal_literal(self):
        """test decimal literals"""
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 119))

    def test_decimal_literal_2(self):
        """test number 0"""
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 120))

    def test_decimal_literal_3(self):
        """test number with leading 0"""
        self.assertTrue(TestLexer.checkLexeme("0012300", "0,0,12300,<EOF>", 121))

    def test_decimal_literal_4(self):
        """test number from 1 to 9"""
        self.assertTrue(
            TestLexer.checkLexeme("1 2 3 4 5 6 7 8 9", "1,2,3,4,5,6,7,8,9,<EOF>", 122)
        )

    def test_binary_literal(self):
        """test binary literals"""
        self.assertTrue(TestLexer.checkLexeme("0b101 0B010", "0b101,0B010,<EOF>", 123))

    def test_binary_literal_2(self):
        """test binary literals with wrong format"""
        self.assertTrue(
            TestLexer.checkLexeme("0b123 0b221", "0b1,23,0,b221,<EOF>", 124)
        )

    def test_octal_literal(self):
        """test octal literals"""
        self.assertTrue(TestLexer.checkLexeme("0o123 0O456", "0o123,0O456,<EOF>", 125))

    def test_octal_literal_2(self):
        """test octal literals with wrong format"""
        self.assertTrue(
            TestLexer.checkLexeme("0o123 0o891 0o759", "0o123,0,o891,0o75,9,<EOF>", 126)
        )

    def test_hexadecimal_literal(self):
        """test hexadecimal literals"""
        self.assertTrue(TestLexer.checkLexeme("0x123 0X456", "0x123,0X456,<EOF>", 127))

    def test_hexadecimal_literal_2(self):
        """test hexadecimal literals with wrong format"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "0x123 0x1s2 0x1g3 0Xg21", "0x123,0x1,s2,0x1,g3,0,Xg21,<EOF>", 128
            )
        )

    # Float
    def test_float_literal(self):
        """test float literals"""
        self.assertTrue(
            TestLexer.checkLexeme("1.2 3.4 5.6e3", "1.2,3.4,5.6e3,<EOF>", 129)
        )

    def test_float_literal_2(self):
        """test float literals with missing optional part"""
        self.assertTrue(TestLexer.checkLexeme("1. 2.e3 4.3", "1.,2.e3,4.3,<EOF>", 130))

    def test_float_literal_3(self):
        """test float literals with wrong format"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "1.2e 3.4e .4e2 3e2 e1 2.3e2.1 1.2.e3",
                "1.2,e,3.4,e,.,4,e2,3,e2,e1,2.3e2,.,1,1.2,.,e3,<EOF>",
                131,
            )
        )

    # String
    def test_string_literal(self):
        """test string literals"""
        self.assertTrue(
            TestLexer.checkLexeme('"abc" "def" "ghi"', '"abc","def","ghi",<EOF>', 132)
        )

    def test_string_literal_2(self):
        """test string literals with escape characters"""
        self.assertTrue(
            TestLexer.checkLexeme(
                '"abc\\n" "def\\t" "ghi\\r"',
                '"abc\\n","def\\t","ghi\\r",<EOF>',
                133,
            )
        )

    def test_string_literal_3(self):
        """Contain all ASCII characters except double quote and backslash"""
        self.assertTrue(
            TestLexer.checkLexeme(
                '"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>?/.,;:[]{}"',
                '"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>?/.,;:[]{}",<EOF>',
                134,
            )
        )

    def test_string_literal_4(self):
        """test string literals include double quote and backslash"""
        self.assertTrue(
            TestLexer.checkLexeme(
                '"abc\\"def" "ghi\\\\"',
                '"abc\\"def","ghi\\\\",<EOF>',
                135,
            )
        )

    # Boolean
    def test_boolean_literal(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("true false", "true,false,<EOF>", 136))

    def test_boolean_literal_2(self):
        """test boolean literals with wrong format"""
        self.assertTrue(TestLexer.checkLexeme("truefalse", "truefalse,<EOF>", 137))

    # Nil
    def test_nil_literal(self):
        """test nil literals"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 138))

    def test_nil_literal_2(self):
        """test nil literals with wrong format"""
        self.assertTrue(TestLexer.checkLexeme("nil123", "nil123,<EOF>", 139))

    # Complex literals
    def test_complex_integer_literal(self):
        """test integer literals go with operators"""
        self.assertTrue(
            TestLexer.checkLexeme("1+2-3*4/5%6", "1,+,2,-,3,*,4,/,5,%,6,<EOF>", 140)
        )

    def test_complex_float_literal(self):
        """test float literals go with operators"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "1.2+3.4-5.6*7.8/9.0", "1.2,+,3.4,-,5.6,*,7.8,/,9.0,<EOF>", 141
            )
        )

    def test_complex_string_literal(self):
        """test string literals go with operators"""
        self.assertTrue(
            TestLexer.checkLexeme(
                '"abc"+"def"-"ghi"*"jkl"/"mno"',
                '"abc",+,"def",-,"ghi",*,"jkl",/,"mno",<EOF>',
                142,
            )
        )

    def test_complex_boolean_literal(self):
        """test boolean literals go with operators"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "true&&false||true", "true,&&,false,||,true,<EOF>", 143
            )
        )

    def test_complex_nil_literal(self):
        """test nil literals go with operators"""
        self.assertTrue(TestLexer.checkLexeme("nil==nil", "nil,==,nil,<EOF>", 144))

    # !-------------------Test if compiler throws errors -------------------!
    def test_invalid_ascii(self):
        """test invalid ascii"""
        self.assertTrue(TestLexer.checkLexeme("a\u0000b", "a,ErrorToken \u0000", 145))

    def test_error_token(self):
        """test error token with ^"""
        self.assertTrue(TestLexer.checkLexeme("a^b", "a,ErrorToken ^", 146))

    def test_error_token_2(self):
        """test error token with @"""
        self.assertTrue(TestLexer.checkLexeme("a@b", "a,ErrorToken @", 147))

    def test_error_token_3(self):
        """test error token with ~"""
        self.assertTrue(TestLexer.checkLexeme("a~b", "a,ErrorToken ~", 148))

    def test_error_token_4(self):
        """test error token with &"""
        self.assertTrue(TestLexer.checkLexeme("a&b", "a,ErrorToken &", 149))

    def test_error_token_5(self):
        """test error token with #"""
        self.assertTrue(TestLexer.checkLexeme("a#b", "a,ErrorToken #", 150))

    def test_error_token_6(self):
        """test error token with $"""
        self.assertTrue(TestLexer.checkLexeme("a$b", "a,ErrorToken $", 151))

    def test_error_token_7(self):
        """test error token with `"""
        self.assertTrue(TestLexer.checkLexeme("a`b", "a,ErrorToken `", 152))

    def test_error_token_8(self):
        """test error token with \ """
        self.assertTrue(TestLexer.checkLexeme("a\\b", "a,ErrorToken \\", 153))

    def test_error_token_9(self):
        """test error token with '"""
        self.assertTrue(TestLexer.checkLexeme("a'b", "a,ErrorToken '", 154))

    def test_error_token_10(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme('"abc\\', 'ErrorToken "', 155))

    def test_unclosed_string(self):
        """test unclosed string end with EOF"""
        self.assertTrue(TestLexer.checkLexeme('"abc', 'Unclosed string: "abc', 156))

    def test_unclosed_string_2(self):
        """test unclosed string end with new line"""
        self.assertTrue(
            TestLexer.checkLexeme('"abc\naaa"', 'Unclosed string: "abc', 157)
        )

    def test_unclosed_string_3(self):
        """test illegal escape character"""
        self.assertTrue(
            TestLexer.checkLexeme('"abc\\"', 'Unclosed string: "abc\\"', 158)
        )

    def test_unclosed_string_4(self):
        """test unclosed string having escape character"""
        self.assertTrue(
            TestLexer.checkLexeme('"abc\\n', 'Unclosed string: "abc\\n', 159)
        )

    def test_illegal_escape(self):
        """test illegal escape character"""
        self.assertTrue(
            TestLexer.checkLexeme(
                '"abc\\abc"', 'Illegal escape in string: "abc\\a', 160
            )
        )

    def test_illegal_escape_2(self):
        """test illegal escape character"""
        self.assertTrue(
            TestLexer.checkLexeme('"abc\\3"', 'Illegal escape in string: "abc\\3', 161)
        )

    # !-------------------Test character sets -------------------!
    def test_space(self):
        """test space"""
        self.assertTrue(TestLexer.checkLexeme(" ", "<EOF>", 162))

    def test_tab(self):
        """test tab"""
        self.assertTrue(TestLexer.checkLexeme("\t", "<EOF>", 163))

    def test_form_feed(self):
        """test form feed"""
        self.assertTrue(TestLexer.checkLexeme("\f", "<EOF>", 164))

    def test_carriage_return(self):
        """test carriage return"""
        self.assertTrue(TestLexer.checkLexeme("\r", "<EOF>", 165))

    # New line is special case, it will turn into ; in some cases
    def test_newline_1(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
    func main() {
        var x int = 10
        var y float = 3.14
        
        if x > 5 {
            y = y * 2
            
        }
        
    }""",
                """func,main,(,),{,var,x,int,=,10,;,var,y,float,=,3.14,;,if,x,>,5,{,y,=,y,*,2,;,},;,},<EOF>""",
                166,
            )
        )

    def test_newline_2(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
    for i := 0; i < 10; i += 1
    {
        print(i)
    }
                """,
                """for,i,:=,0,;,i,<,10,;,i,+=,1,;,{,print,(,i,),;,},;,<EOF>""",
                167,
            )
        )

    def test_newline_3(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
                
    var a int
    var b float
    b = 3.14
                """,
                """var,a,int,;,var,b,float,;,b,=,3.14,;,<EOF>""",
                168,
            )
        )

    def test_newline_4(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
    func add(x int, y int) int
    {
        return x + y
    }
                """,
                """func,add,(,x,int,,,y,int,),int,;,{,return,x,+,y,;,},;,<EOF>""",
                169,
            )
        )

    def test_newline_5(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
    type Car struct {
        brand string
        year int
    }

    var myCar Car""",
                """type,Car,struct,{,brand,string,;,year,int,;,},;,var,myCar,Car,<EOF>""",
                170,
            )
        )

    def test_newline_6(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
    if a == 5 
    {
        b = 10
    }
                """,
                """if,a,==,5,;,{,b,=,10,;,},;,<EOF>""",
                171,
            )
        )

    def test_newline_7(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
    x := 5
    y := x + 2
    z := y * 3
                """,
                """x,:=,5,;,y,:=,x,+,2,;,z,:=,y,*,3,;,<EOF>""",
                172,
            )
        )

    def test_newline_8(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
    var a int = 42
    var b int = a + 10""",
                """var,a,int,=,42,;,var,b,int,=,a,+,10,<EOF>""",
                173,
            )
        )

    def test_newline_9(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
    const PI = 3.1415
    var radius float = 10.0
    var area float = PI * radius * radius""",
                """const,PI,=,3.1415,;,var,radius,float,=,10.0,;,var,area,float,=,PI,*,radius,*,radius,<EOF>""",
                174,
            )
        )

    def test_newline_10(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
    switch choice {
    case 1:
        print("Option 1")
    case 2:
        print("Option 2")
    }""",
                """switch,choice,{,case,1,:,print,(,"Option 1",),;,case,2,:,print,(,"Option 2",),;,},<EOF>""",
                175,
            )
        )

    def test_newline_11(self):
        """test newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """
    var arr [5]int = [5]int{1, 2, 3, 4, 5}
    for _, val := range arr 
    {
        print(val)
    }""",
                "var,arr,[,5,],int,=,[,5,],int,{,1,,,2,,,3,,,4,,,5,},;,for,_,,,val,:=,range,arr,;,{,print,(,val,),;,},<EOF>",
                176,
            )
        )

    # !-------------------Test comments -------------------!

    def test_nested_comment_1(self):
        """Test nested block comments"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """/* Outer comment /* Inner comment */ Still outer */ valid_token""",
                """valid_token,<EOF>""",
                177,
            )
        )

    def test_nested_comment_2(self):
        """Test deeply nested block comments"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """/* Level 1 /* Level 2 /* Level 3 */ Back to level 2 */ Back to level 1 */ code_here""",
                """code_here,<EOF>""",
                178,
            )
        )

    def test_nested_comment_3(self):
        """Test unterminated nested comment"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """/* Unfinished /* Nested level */ Still open""",
                """Still,open,<EOF>""",
                179,
            )
        )

    def test_line_comment_1(self):
        """Test line comment"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """// This is a line comment""",
                """<EOF>""",
                180,
            )
        )

    def test_line_comment_2(self):
        """Test line comment"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """// This is a line comment
                valid_token""",
                """valid_token,<EOF>""",
                181,
            )
        )

    def test_line_comment_with_nested_comment(self):
        """Test line comment in block comment"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """/* This is a block comment // with line comment inside */ valid_token""",
                """valid_token,<EOF>""",
                182,
            )
        )

    def test_many_nested_comments(self):
        """Test many nested comments with the code between them"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """/* Level 1 /* Level 2 /* Level 3 */ Back to level 2 */ Back to level 1 */ code_here /* Another comment */""",
                """code_here,<EOF>""",
                183,
            )
        )

    def test_line_comment_with_nested_comment_2(self):
        """Test line comment with nested block comment"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """// This is a line comment /* Nested block comment */ valid_token""",
                """<EOF>""",
                184,
            )
        )

    def test_line_comment_with_nested_comment_3(self):
        """Test line comment with nested block comment and newline"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """// This is a line comment /* Nested block comment 
                hello */ valid_token""",
                """hello,*,/,valid_token,<EOF>""",
                185,
            )
        )

    # !-------------------Advanced tests -------------------!
    def test_illegal_escape_3(self):
        """test illegal escape character"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """ "\\" \\\\ \\q" """, 'Illegal escape in string: "\\" \\\\ \\q', 186
            )
        )

    def test_unclosed_comment(self):
        """test unclosed comment"""
        self.assertTrue(
            TestLexer.checkLexeme(
                """/* Unclosed comment""", "/,*,Unclosed,comment,<EOF>", 187
            )
        )

    def test_very_long_identifier(self):
        """test very long identifier"""
        self.assertTrue(TestLexer.checkLexeme("a" * 1000, "a" * 1000 + ",<EOF>", 188))

    def test_separator_4(self):
        """test separators with new line"""
        self.assertTrue(TestLexer.checkLexeme("(){},;", "(,),{,},,,;,<EOF>", 189))

    def test_operator_4(self):
        """test with expression"""
        self.assertTrue(
            TestLexer.checkLexeme("1+2-3*4/5%6", "1,+,2,-,3,*,4,/,5,%,6,<EOF>", 190)
        )

    def test_operator_5(self):
        """test with expression"""
        self.assertTrue(
            TestLexer.checkLexeme("1+2-3*4/5%6", "1,+,2,-,3,*,4,/,5,%,6,<EOF>", 191)
        )

    def test_negative_number(self):
        """test negative number"""
        self.assertTrue(TestLexer.checkLexeme("-123", "-,123,<EOF>", 192))

    def test_negative_float(self):
        """test negative float"""
        self.assertTrue(TestLexer.checkLexeme("-123.456", "-,123.456,<EOF>", 193))

    def test_not_operator(self):
        """test not operator"""
        self.assertTrue(TestLexer.checkLexeme("!true", "!,true,<EOF>", 194))

    def test_advanced_1(self):
        """test advanced"""
        input = """func main() {
            if () {
                a := 10;
            }
        }"""
        expect = """func,main,(,),{,if,(,),{,a,:=,10,;,},;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

    def test_advanced_2(self):
        """test advanced"""
        input = """func main() {
            if (a > b) {
                a := 10;
            }
        }"""
        expect = """func,main,(,),{,if,(,a,>,b,),{,a,:=,10,;,},;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))
        
        
    def test_advanced_3(self):
        """Test advanced"""
        input = """func main() {
            for _, value := range a {
                a := value;
            }
        };"""
        expect = """func,main,(,),{,for,_,,,value,:=,range,a,{,a,:=,value,;,},;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))
        
    def test_advanced_4(self):
        """Test advanced"""
        input = """func main() {
            for i := 0; i < 10; i += 1 {
                print(i);
            }
        }"""
        expect = """func,main,(,),{,for,i,:=,0,;,i,<,10,;,i,+=,1,{,print,(,i,),;,},;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))
        
    def test_advanced_5(self):
        input = """func main() {
            a.foo(b);
        }"""
        expect = """func,main,(,),{,a,.,foo,(,b,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))
        
    def test_advanced_6(self):
        input = """func main() {
            a[1] = 2;
        }"""
        expect = """func,main,(,),{,a,[,1,],=,2,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))