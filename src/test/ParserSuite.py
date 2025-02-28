import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # ! ------------------- Sample test ------------------- !
    def test_simple_program(self):
        """Simple program: void main() {}"""
        input = """func main() {
                say("Hello, world!");
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
            a := 1;
            b := 2;
            return a + b;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    # ! ------------------- Program structure 2 ------------------- !
    def test_program_structure(self):
        """Program with many declaration"""
        input = """var a int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_program_structure_2(self):
        """Invalid program with statement"""
        input = """a := 1;"""
        expect = "Error on line 1 col 1: a"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_program_structure_3(self):
        """Invalid program with for statement"""
        input = """for a := 1 to 10 do {}"""
        expect = "Error on line 1 col 1: for"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_program_structure_4(self):
        """Invalid program with if statement"""
        input = """if a == 1 then {}"""
        expect = "Error on line 1 col 1: if"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_program_structure_5(self):
        """Valid program with struct declaration"""
        input = """type a struct {
            name string;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    #! ------------------- Declaration ------------------- !
    def test_variable_declaration(self):
        """Variable declaration"""
        input = """var a int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_variable_declaration_2(self):
        """Multiple variable declaration"""
        input = """var a,b,c int;"""
        expect = "Error on line 1 col 6: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_variable_declaration_3(self):
        """Variable declaration with assignment"""
        input = """var a int = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_variable_declaration_4(self):
        """Variable declaration with inferred type"""
        input = """var a = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_variable_declaration_5(self):
        """Variable declaration with not specify type and initial value"""
        input = """var a;"""
        expect = "Error on line 1 col 6: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_variable_declaration_6(self):
        """Variable declaration with composite type"""
        input = """var a = Person{name:"name", age: 20};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_invalid_variable_declaration(self):
        """Invalid variable declaration"""
        input = """var a;"""
        expect = "Error on line 1 col 6: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_constant_declaration(self):
        """Constant declaration"""
        input = """const a = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_constant_declaration_2(self):
        """Constant struct declaration"""
        input = """const a = Person{name:"name", age: 20};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_invalid_constant_declaration(self):
        """Invalid constant declaration"""
        input = """const a = 1"""
        expect = "Error on line 1 col 12: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_invalid_constant_declaration_2(self):
        """Missing right hand side"""
        input = """const a;"""
        expect = "Error on line 1 col 8: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_function_declaration(self):
        """Function declaration"""
        input = """func main() {
                a:= 1;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_function_declaration_2(self):
        """Function declaration with parameter"""
        input = """func main(a int) {
                a:= 1;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_function_declaration_3(self):
        """Function declaration with return type"""
        input = """func main() int {
                return 1;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_function_declaration_4(self):
        """Function declaration with body statement"""
        input = """func main() {a := 1;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_function_declaration_5(self):
        """Function declaration with return type, parameters and body statement"""
        input = """func main(a int) int {return 1;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_method_declaration(self):
        """Method declaration"""
        input = """func (a Person) main() {
                a:= 1;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_method_declaration_2(self):
        """Method declaration with parameter"""
        input = """func (a Person) main(b int) {
                a:= 1;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_method_declaration_3(self):
        """Method declaration with return type"""
        input = """func (a Person) main() int {
                return 1;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_method_declaration_4(self):
        """Method declaration with body statement"""
        input = """func (a Person) main() {a := 1;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_method_declaration_5(self):
        """Method declaration with return type, parameters and body statement"""
        input = """func (a Person) main(b int) int {return 1;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_invalid_function_declaration(self):
        """Missing function identifier"""
        input = """func () {};"""
        expect = "Error on line 1 col 7: )"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_invalid_function_declaration_2(self):
        """Nested function declaration"""
        input = """func main() {func foo() {};};"""
        expect = "Error on line 1 col 14: func"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_invalid_function_declaration_3(self):
        """Missing function body"""
        input = """func main();"""
        expect = "Error on line 1 col 12: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_invalid_function_declaration_4(self):
        """Missing function body statement"""
        input = """func main() {};"""
        expect = "Error on line 1 col 14: }"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_invalid_method_declaration_2(self):
        """Nested method declaration"""
        input = """func (a Person) main() {func foo() {};};"""
        expect = "Error on line 1 col 25: func"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_invalid_method_declaration_3(self):
        """Missing method body"""
        input = """func (a Person) main();"""
        expect = "Error on line 1 col 23: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_invalid_method_declaration_4(self):
        """Missing struct type"""
        input = """func (a) main() {};"""
        expect = "Error on line 1 col 8: )"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_struct_declaration(self):
        """Struct declaration"""
        input = """type Person struct {};"""
        expect = "Error on line 1 col 21: }"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_struct_declaration_2(self):
        """Struct declaration with field"""
        input = """type Person struct {name string; age int;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_invalid_struct_declaration(self):
        """Missing struct identifier"""
        input = """type struct {};"""
        expect = "Error on line 1 col 6: struct"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_invalid_struct_declaration_2(self):
        """Missing struct body"""
        input = """type Person struct;"""
        expect = "Error on line 1 col 19: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_invalid_struct_declaration_3(self):
        """Missing struct keyword"""
        input = """Person struct {};"""
        expect = "Error on line 1 col 1: Person"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_interface_declaration(self):
        """Interface declaration"""
        input = """type Person interface {
            Hello();
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_interface_declaration_2(self):
        """Interface declaration with method"""
        input = """type Person interface {Hello();};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_interface_declaration_3(self):
        """Interface declaration with method and return type"""
        input = """type Person interface {Hello() int;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_invalid_interface_declaration(self):
        """Missing interface identifier"""
        input = """type interface {};"""
        expect = "Error on line 1 col 6: interface"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_invalid_interface_declaration_2(self):
        """Missing interface body"""
        input = """type Person interface;"""
        expect = "Error on line 1 col 22: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_invalid_interface_declaration_3(self):
        """Missing interface keyword"""
        input = """Person interface {};"""
        expect = "Error on line 1 col 1: Person"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    #! ------------------- Literal ------------------- !
    def test_integer_literal(self):
        """Integer literal"""
        input = """const a = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_integer_literal_2(self):
        """Negative integer literal"""
        input = """const a = -1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_boolean_literal(self):
        """Boolean literal"""
        input = """const a = true;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_float_literal(self):
        """Float literal"""
        input = """const a = 1.0;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_string_literal(self):
        """String literal"""
        input = """const a = "Hello";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_array_literal(self):
        """Array literal"""
        input = """const a = [3]int{10, 20, 30};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_array_literal_2(self):
        """Multi-dimensional array literal"""
        input = """const a = [3][2]int{{1, 2}, {3, 4}, {5, 6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_struct_literal(self):
        """Struct literal"""
        input = """const a = Person{name:"name", age: 20};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_nil_literal(self):
        """Nil literal"""
        input = """const a = nil;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    #! ------------------- Expression ------------------- !
    def test_identifier_expression(self):
        """Identifier expression"""
        input = """const a = b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_array_element_expression(self):
        """Array element expression"""
        input = """const a = b[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_array_element_expression_2(self):
        """Array element expression with expression index"""
        input = """const a = b[1 + 2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_array_element_expression_3(self):
        """Multi-dimensional array element expression"""
        input = """const a = b[1][2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_struct_field_expression(self):
        """Struct field expression"""
        input = """const a = b.name;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_struct_field_expression_2(self):
        """Nested struct field expression"""
        input = """const a = b.c.d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_function_call_expression(self):
        """Function call expression"""
        input = """const a = foo();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_method_call_expression(self):
        """Method call expression"""
        input = """const a = b.foo();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_unary_expression(self):
        """Unary expression"""
        input = """const a = -b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_binary_expression(self):
        """Binary expression"""
        input = """const a = b + c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_large_expression(self):
        """Large expression"""
        input = """const a = b + c * d / e % f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_expression_with_parentheses(self):
        """Expression with parentheses"""
        input = """const a = (b + c) * d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_relational_expression(self):
        """Relational expression with ==, !=, <, >, <=, >= operator"""
        input = """const a = b > c == d >= e != g < h == i <=j;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_logical_expression(self):
        """Logical expression with &&, ||, ! operator"""
        input = """const a = b && c || d && !e;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_invalid_expression(self):
        """Invalid expression"""
        input = """const a = b +;"""
        expect = "Error on line 1 col 14: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_invalid_expression_2(self):
        """Missing expression"""
        input = """const a = ;"""
        expect = "Error on line 1 col 11: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_invalid_expression_3(self):
        """Missing parentheses"""
        input = """const a = (b + c;"""
        expect = "Error on line 1 col 17: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_invalid_expression_4(self):
        """Missing operator"""
        input = """const a = b c;"""
        expect = "Error on line 1 col 13: c"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_invalid_expression_5(self):
        """Missing left hand side"""
        input = """const a = + b;"""
        expect = "Error on line 1 col 11: +"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_invalid_expression_6(self):
        """Missing index"""
        input = """const a = b[];"""
        expect = "Error on line 1 col 13: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_invalid_expression_7(self):
        """Missing field"""
        input = """const a = b.;"""
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_invalid_expression_8(self):
        """Wrong operator"""
        input = """const a = b & c;"""
        expect = "&"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_invalid_expression_9(self):
        """Missing parameter after comma"""
        input = """const a = foo(a,);"""
        expect = "Error on line 1 col 17: )"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_invalid_expression_10(self):
        """Missing parameter"""
        input = """const a = foo(,);"""
        expect = "Error on line 1 col 15: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_invalid_expression_11(self):
        """Missing method after dot"""
        input = """const a = b.;"""
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_invalid_expression_12(self):
        """Using wrong operator when assign value"""
        input = """const a = b = c;"""
        expect = "Error on line 1 col 13: ="
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    #! ------------------- Statement 7 ------------------- !
    def test_declaration_statement(self):
        """Variable declaration statement"""
        input = """func main() {var a int;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_declaration_statement_2(self):
        """Constant declaration statement"""
        input = """func main() {a := 1;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_declaration_statement_3(self):
        """Cannot have function declaration statement"""
        input = """func main() {func foo() {};};"""
        expect = "Error on line 1 col 14: func"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_declaration_statement_4(self):
        """Cannot have method declaration statement"""
        input = """func main() {func (a Person) foo() {};};"""
        expect = "Error on line 1 col 14: func"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_declaration_statement_5(self):
        """Cannot have struct declaration statement"""
        input = """func main() {type Person struct {};};"""
        expect = "Error on line 1 col 14: type"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_declaration_statement_6(self):
        """Cannot have interface declaration statement"""
        input = """func main() {type Person interface {};};"""
        expect = "Error on line 1 col 14: type"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_assignment_statement(self):
        """Assignment statement"""
        input = """func main() {a := 1;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_assignment_statement_2(self):
        """Wrong assignment operator"""
        input = """func main() {a = 1;};"""
        expect = "Error on line 1 col 16: ="
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_assignment_statement_3(self):
        """Assignment statement with expression"""
        input = """func main() {a := b + c;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_assignment_statement_4(self):
        """Assignment with +=, -=, *=, /=, %= operator"""
        input = """func main() {a += b; a -= c; a *= d; a /= e; a %= f;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_assignment_statement_5(self):
        """Missing right hand side"""
        input = """func main() {a := ;};"""
        expect = "Error on line 1 col 19: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_assignment_statement_6(self):
        """Missing left hand side"""
        input = """func main() { := 1;};"""
        expect = "Error on line 1 col 15: :="
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_assignment_statement_7(self):
        """Missing operator"""
        input = """func main() {a b;};"""
        expect = "Error on line 1 col 16: b"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_if_statement(self):
        """If statement"""
        input = """func main() {
            if (a == 1) {
                a := 10;
            } else if (a >= 1) {
                a := 20;
            } else {
                a := 30;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_if_statement_2(self):
        """If statement without else"""
        input = """func main() {
            if (a == 1) {
                a := 10;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_if_statement_3(self):
        """If statement without else if"""
        input = """func main() {
            if (a == 1) {
                a := 10;
            } else {
                a := 20;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test_if_statement_4(self):
        """If statement with if and else if no else"""
        input = """func main() {
            if (a == 1) {
                a := 10;
            } else if (a >= 1) {
                a := 20;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 301))

    def test_if_statement_5(self):
        """Missing condition"""
        input = """func main() {
            if () {
                a := 10;
            }
        };"""
        expect = "Error on line 2 col 17: )"
        self.assertTrue(TestParser.checkParser(input, expect, 302))

    def test_if_statement_6(self):
        """Missing body"""
        input = """func main() {
            if (a == 1);
        };"""
        expect = "Error on line 2 col 24: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 303))

    def test_if_statement_7(self):
        """Missing parentheses"""
        input = """func main() {
            if a == 1 {
                a := 10;
            }
        };"""
        expect = "Error on line 2 col 16: a"
        self.assertTrue(TestParser.checkParser(input, expect, 304))

    def test_if_statement_8(self):
        """Missing braces"""
        input = """func main() {
            if (a == 1)
                a := 10;
        };"""
        expect = "Error on line 2 col 24: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 305))

    def test_if_statement_9(self):
        """The left brace should be on the same line with if"""
        input = """func main() 
            if (a == 1) 
            {
                a := 10;
            }
        };"""
        expect = "Error on line 1 col 14: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 306))

    def test_for_statement(self):
        """Basic for statement"""
        input = """func main() {
            for i < 10 {
                a := i;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 307))

    def test_for_statement_2(self):
        """For statement with init statement"""
        input = """func main() {
            for i := 0; i < 10; i+=1 {
                a := i;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 308))

    def test_for_statement_3(self):
        """For statement with range"""
        input = """func main() {
            for i, value := range a {
                a := value;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 309))

    def test_for_statement_4(self):
        """For statement with underscore"""
        input = """func main() {
            for _, value := range a {
                a := value;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 310))

    def test_for_statement_5(self):
        """Basic for with invalid expression"""
        input = """func main() {
            for int {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 17: int"
        self.assertTrue(TestParser.checkParser(input, expect, 311))

    def test_for_statement_6(self):
        """For statement with wrong range operator"""
        input = """func main() {
            for i, value = range a {
                a := value;
            }
        };"""
        expect = "Error on line 2 col 26: ="
        self.assertTrue(TestParser.checkParser(input, expect, 312))

    def test_for_statement_7(self):
        """For statement with missing keyword range"""
        input = """func main() {
            for i, value := a {
                a := value;
            }
        };"""
        expect = "Error on line 2 col 29: a"
        self.assertTrue(TestParser.checkParser(input, expect, 313))

    def test_for_statement_8(self):
        """For statement with missing range name"""
        input = """func main() {
            for i, value := range {
                a := value;
            }
        };"""
        expect = "Error on line 2 col 35: {"
        self.assertTrue(TestParser.checkParser(input, expect, 314))

    def test_for_statement_9(self):
        """For statement with assignment initialization"""
        input = """func main() {
            for i := 0; i < 10; i+=1 {
                a := i;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 315))

    def test_for_statement_10(self):
        """For statement with declaration initialization"""
        input = """func main() {
            for var i int = 0; i < 10; i+=1 {
                a := i;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 316))

    def test_for_statement_11(self):
        """For statement with wrong initialization: constant declaration"""
        input = """func main() {
            for const i = 0; i < 10; i+=1 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 17: const"
        self.assertTrue(TestParser.checkParser(input, expect, 317))

    def test_for_statement_12(self):
        """For statement with wrong initialization: expression"""
        input = """func main() {
            for true; i < 10; i+=1 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 21: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 318))

    def test_for_statement_13(self):
        """For statement with wrong initialization: if statement"""
        input = """func main() {
            for if (true) {}; i+=1 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 17: if"
        self.assertTrue(TestParser.checkParser(input, expect, 319))

    def test_for_statement_14(self):
        """For statement with wrong condition: declaration statement"""
        input = """func main() {
            for i := 0; var j int = 10; i+=1 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 25: var"
        self.assertTrue(TestParser.checkParser(input, expect, 320))

    def test_for_statement_15(self):
        """For statement with wrong condition: assignment statement"""
        input = """func main() {
            for i := 0; j := 10; i+=1 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 27: :="
        self.assertTrue(TestParser.checkParser(input, expect, 321))

    def test_for_statement_16(self):
        """For statement with wrong condition: if statement"""
        input = """func main() {
            for i := 0; if (true) {}; i+=1 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 25: if"
        self.assertTrue(TestParser.checkParser(input, expect, 322))

    def test_for_statement_17(self):
        """For statement with wrong update: declaration statement"""
        input = """func main() {
            for i := 0; i < 10; var j int {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 33: var"
        self.assertTrue(TestParser.checkParser(input, expect, 323))

    def test_for_statement_18(self):
        """For statement with wrong update: expression"""
        input = """func main() {
            for i := 0; i < 10; true {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 33: true"
        self.assertTrue(TestParser.checkParser(input, expect, 324))

    def test_for_statement_19(self):
        """For statement with wrong update: if statement"""
        input = """func main() {
            for i := 0; i < 10; if (true) {} {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 33: if"
        self.assertTrue(TestParser.checkParser(input, expect, 325))

    def test_for_statement_20(self):
        """For statement with missing 1 of 3 parts"""
        input = """func main() {
            for i < 10; i+=1 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 23: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 326))

    def test_for_statement_21(self):
        """Basic for with wrong expression: declaration statement"""
        input = """func main() {
            for var i int = 0 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 31: {"
        self.assertTrue(TestParser.checkParser(input, expect, 327))

    def test_for_statement_22(self):
        """Basic for with wrong expression: assignment statement"""
        input = """func main() {
            for i := 0 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 24: {"
        self.assertTrue(TestParser.checkParser(input, expect, 328))

    #! ------------------- Break, Continue, Return ------------------- !
    def test_break_statement(self):
        """Break statement"""
        input = """func main() {
            for i < 10 {
                break;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 329))

    def test_break_statement_2(self):
        """Cannot assign break to a variable"""
        input = """func main() {
            for i < 10 {
                a := break;
            }
        };"""
        expect = "Error on line 3 col 22: break"
        self.assertTrue(TestParser.checkParser(input, expect, 330))

    def test_continue_statement(self):
        """Continue statement"""
        input = """func main() {
            for i < 10 {
                continue;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 331))

    def test_continue_statement_2(self):
        """Cannot assign continue to a variable"""
        input = """func main() {
            for i < 10 {
                a := continue;
            }
        };"""
        expect = "Error on line 3 col 22: continue"
        self.assertTrue(TestParser.checkParser(input, expect, 332))

    def test_return_statement(self):
        """Return statement"""
        input = """func main() {
            return 1;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 333))

    def test_return_statement_2(self):
        """Return statement with expression"""
        input = """func main() {
            return a;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 334))

    def test_return_statement_3(self):
        """Return statement with no expression"""
        input = """func main() {
            return;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 335))

    def test_return_statement_4(self):
        """Cannot assign return to a variable"""
        input = """func main() {
            a := return;
        };"""
        expect = "Error on line 2 col 18: return"
        self.assertTrue(TestParser.checkParser(input, expect, 336))

    #! ------------------- Call statement ------------------- !
    def test_call_statement(self):
        """Call statement"""
        input = """func main() {
            foo();
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 337))

    def test_call_statement_2(self):
        """Call statement with parameter"""
        input = """func main() {
            foo(a);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 338))

    def test_call_statement_3(self):
        """Call statement with multiple parameters"""
        input = """func main() {
            foo(a, b, c);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 339))

    def test_call_statement_4(self):
        """Call statement with expression"""
        input = """func main() {
            foo(a + b);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 340))

    def test_call_statement_5(self):
        """Call statement with nested call"""
        input = """func main() {
            foo(bar());
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 341))

    def test_call_statement_6(self):
        """Call statement with method call"""
        input = """func main() {
            a.foo();
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 342))

    def test_call_statement_7(self):
        """Call statement with method call with parameter"""
        input = """func main() {
            a.foo(b);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 343))

    def test_call_statement_8(self):
        """Call statement with method call with multiple parameters"""
        input = """func main() {
            a.foo(b, c, d);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 344))

    def test_call_statement_9(self):
        """Call statement with method call with expression"""
        input = """func main() {
            a.foo(b + c);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 345))

    def test_call_statement_10(self):
        """Call statement with method call with nested call"""
        input = """func main() {
            a.foo(bar());
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 346))

    def test_call_statement_11(self):
        """Call statement with method call with method call"""
        input = """func main() {
            a.foo().bar();
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 347))

    def test_call_statement_12(self):
        """Call statement with method call with method call with parameter"""
        input = """func main() {
            a.foo().bar(b);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 348))

    def test_call_statement_13(self):
        """Call statement with method call with method call with multiple parameters"""
        input = """func main() {
            a.foo().bar(b, c, d);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 349))

    def test_call_statement_14(self):
        """Assign call statement to a variable"""
        input = """func main() {
            a := foo();
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 350))

    def test_call_statement_15(self):
        """Assign call statement to a variable with parameter"""
        input = """func main() {
            a := foo(b);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 351))

    def test_call_statement_16(self):
        """Method call as a parameter"""
        input = """func main() {
            foo(a.foo());
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 352))

    def test_call_statement_17(self):
        """Method call as a parameter with parameter"""
        input = """func main() {
            foo(a.foo(b));
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 353))

    def test_call_statement_18(self):
        """Method call as a parameter with multiple parameters"""
        input = """func main() {
            foo(a.foo(b, c, d));
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 354))

    def test_call_statement_19(self):
        """Wrong call statement: missing parentheses"""
        input = """func main() {
            foo;
        };"""
        expect = "Error on line 2 col 16: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 355))

    def test_call_statement_20(self):
        """Wrong call statement: Missing identifier after comma seperator of parameters"""
        input = """func main() {
            foo(a, );
        };"""
        expect = "Error on line 2 col 20: )"
        self.assertTrue(TestParser.checkParser(input, expect, 356))

    def test_call_statement_21(self):
        """Wrong call statement: Missing identifier after comma seperator of parameters"""
        input = """func main() {
            foo(, a);
        };"""
        expect = "Error on line 2 col 17: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 357))

    #! ------------------- Block statement ------------------- !
    def test_block_statement(self):
        """Block statement"""
        input = """func main() {
                a := 1;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 358))

    def test_block_statement_2(self):
        """Block statement with multiple statements"""
        input = """func main() {
                a := 1;
                b := 2;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 359))

    def test_block_statement_3(self):
        """Block statement with multiple statements separated by newline"""
        input = """func main() {
                a := 1;
                b := 2;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 360))

    def test_block_statement_4(self):
        """Statements not separated by semicolon and newline"""
        input = """func main() {
                a := 1, b := 2
        };"""
        expect = "Error on line 2 col 23: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 361))

    #! ------------------- Newline ------------------- !
    def test_newline(self):
        """Newline"""
        input = """func main() {
                a := 1
                b := 2
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 362))

    def test_newline_2(self):
        """Newline with empty line"""
        input = """func main() {
                a := 1

                b := 2
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 363))

    def test_newline_3(self):
        """Many declarations with newline"""
        input = """var a int
        
        const b = 1
        
        func main() {
            a := 1
            b := 2
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 364))

    def test_newline_4(self):
        """Struct with newline"""
        input = """type Person struct {
            name string
            age int
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 365))

    def test_newline_5(self):
        """Interface with newline"""
        input = """type Person interface {
            Hello()
            Hi() int
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 366))

    def test_newline_6(self):
        """For statement with newline"""
        input = """func main() {
            for i < 10 {
                a := i
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 367))

    #! ------------------- Comments ------------------- !
    def test_single_line_comment(self):
        """Single line comment"""
        input = """// This is a comment
        func main() {
            a := 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 368))

    def test_single_line_comment_2(self):
        """Single line comment with newline"""
        input = """// This is a comment

        func main() {
            a := 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 369))

    def test_single_line_comment_3(self):
        """Single line of single line comment"""
        input = """// This is a comment
        // This is another comment
        func main() {
            a := 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 370))

    def test_single_line_comment_4(self):
        """Single line of single line comment with newline"""
        input = """// This is a comment
        // This is another comment

        func main() {
            a := 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 371))

    def test_multi_line_comment(self):
        """Multi line comment"""
        input = """/* This is a comment */
        func main() {
            a := 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 372))

    def test_multi_line_comment_2(self):
        """Multi line comment with newline"""
        input = """/* This is a comment */

        func main() {
            a := 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 373))

    def test_multi_line_comment_3(self):
        """Multi line of multi line comment"""
        input = """/* This is a comment */
        /* This is another comment */
        func main() {
            a := 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 374))

    def test_multi_line_comment_4(self):
        """Nested multi line comment"""
        input = """/* This is a comment /* This is a nested comment */ */
        func main() {
            a := 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 375))

    def test_multi_line_comment_5(self):
        """Two nested multi line comment with the code in between"""
        input = """/* This is a comment /* This is a nested comment */ */
        func main() {
            a := 1
        }
        /* This is another comment */
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 376))

    #! ------------------- Mix ------------------- !
    def test_negative_numbers_with_not_operator(self):
        """Negative numbers with not operator"""
        input = """func main() {
            a := !-1 == 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 377))

    def test_multiply_with_negative_numbers(self):
        """Multiply with negative numbers"""
        input = """func main() {
            a := -1 * -1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 378))

    def test_method_call_with_expression_followed_by_dot(self):
        """Method call with expression followed by dot"""
        input = """func main() {
            a := foo(1).bar();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 379))

    def test_method_call_with_expression_followed_by_dot_2(self):
        """Method call with expression followed by dot"""
        input = """func main() {
            a := (b + c * d).foo();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 380))

    #! ------------------- More tests ------------------- !

    def test_invalid_method_declaration(self):
        """Missing method identifier"""
        input = """func (a Person) () {};"""
        expect = "Error on line 1 col 17: ("
        self.assertTrue(TestParser.checkParser(input, expect, 381))

    def test_invalid_method_declaration_5(self):
        """Missing method body statement"""
        input = """func (a Person) main() {};"""
        expect = "Error on line 1 col 25: }"
        self.assertTrue(TestParser.checkParser(input, expect, 382))

    def test_invalid_interface_declaration4(self):
        """Missing interface body method"""
        input = """type Person interface {};"""
        expect = "Error on line 1 col 24: }"
        self.assertTrue(TestParser.checkParser(input, expect, 383))

    def test_empty_sub_array_literal(self):
        """Empty sub array literal"""
        input = """func main() {
                a := [2][3] int{{}, {}};
            }"""
        expect = "Error on line 2 col 34: }"
        self.assertTrue(TestParser.checkParser(input, expect, 384))

    def test_for_statement_with_scalar(self):
        """For statement with non-scalar initialization"""
        input = """func main() {
            for a[1] := 0; i < 10; i+=1 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 22: :="
        self.assertTrue(TestParser.checkParser(input, expect, 385))

    def test_for_statement_with_scalar_2(self):
        """For statement with non-scalar initialization: attribute assignment"""
        input = """func main() {
            for a.b := 0; i < 10; i+=1 {
                    a := i;
                }
            }"""
        expect = "Error on line 2 col 21: :="
        self.assertTrue(TestParser.checkParser(input, expect, 386))

    def test_for_statement_with_scalar_3(self):
        """For statement with non-scalar update"""
        input = """func main() {
            for i := 0; a[1]; i[1]+=1 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 32: ["
        self.assertTrue(TestParser.checkParser(input, expect, 387))

    def test_for_statement_with_scalar_4(self):
        """For statement with non-scalar update: attribute assignment"""
        input = """func main() {
            for i := 0; i < 10; a.b += 1 {
                    a := i;
                }
            }"""
        expect = "Error on line 2 col 34: ."
        self.assertTrue(TestParser.checkParser(input, expect, 388))

    def test_for_statement_with_scalar_5(self):
        """For range statement with non-scalar index"""
        input = """func main() {
            for a[1], value := range a {
                a := value;
            }
        };"""
        expect = "Error on line 2 col 21: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 389))

    def test_for_statement_with_scalar_6(self):
        """For range statement with non-scalar index: attribute assignment"""
        input = """func main() {
            for a.b, value := range a {
                a := value;
            }
        };"""
        expect = "Error on line 2 col 20: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 390))

    def test_for_statement_with_scalar_7(self):
        """For range statement with non-scalar value"""
        input = """func main() {
            for i, a[1] := range a {
                a := value;
            }
        };"""
        expect = "Error on line 2 col 21: ["
        self.assertTrue(TestParser.checkParser(input, expect, 391))

    def test_for_statement_with_scalar_8(self):
        """For range statement with non-scalar value: attribute assignment"""
        input = """func main() {
            for i, a.b := range a {
                a := value;
            }
        };"""
        expect = "Error on line 2 col 21: ."
        self.assertTrue(TestParser.checkParser(input, expect, 392))

    def test_array_var_declaration(self):
        """Array declaration"""
        input = """func main() {
            var a [2] int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 393))

    def test_array_var_declaration_2(self):
        """Array declaration with array literal"""
        input = """func main() {
            var a [2] int = [2] int{1, 2};
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 394))

    def test_index_is_octal(self):
        """Index is octal"""
        input = """func main() {
            a := b[0o12];
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 395))
        
    def test_index_is_hex(self):
        """Index is hex"""
        input = """func main() {
            a := b[0x12];
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 396))
        
    def test_index_is_bin(self):
        """Index is bin"""
        input = """func main() {
            a := b[0b101];
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 397))
        
    def test_array_literal_contain_expression(self):
        """Array literal contain expression"""
        input = """func main() {
            a := [2] int{1 + 2, 3 * 4};
        };"""
        expect = "Error on line 2 col 28: +"
        self.assertTrue(TestParser.checkParser(input, expect, 398))
        
    def test_array_literal_contain_identifier(self):
        """Array literal contain identifier"""
        input = """func main() {
            a := [2] int{a, b};
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 399))
        
    def test_array_literal_contain_wrong_array_literal(self):
        """Array literal contain wrong array literal"""
        input = """func main() {
            a := [2] int{[2] int{1, 2}, [2] int{3, 4}};
        };"""
        expect = "Error on line 2 col 26: ["
        self.assertTrue(TestParser.checkParser(input, expect, 400))