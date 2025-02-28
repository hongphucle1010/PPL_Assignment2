import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    #! ------------------ Test Declaration ------------------
    def test_var_declaration_1(self):
        input = """var a int;"""
        expect = str(Program([VarDecl("a", IntType(), None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_var_declaration_2(self):
        input = """var a int = 1;"""
        expect = str(Program([VarDecl("a", IntType(), IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_var_declaration_3(self):
        input = """var a = 1;"""
        expect = str(Program([VarDecl("a", None, IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_var_declaration_4(self):
        input = """var a = Person{name:"name", age: 20};"""
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        None,
                        StructLiteral(
                            "Person",
                            [("name", StringLiteral("name")), ("age", IntLiteral(20))],
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_const_declaration_1(self):
        input = """const a = 1;"""
        expect = str(Program([ConstDecl("a", None, IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_const_declaration_2(self):
        input = """const a = Person{name:"name", age: 20};"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        StructLiteral(
                            "Person",
                            [("name", StringLiteral("name")), ("age", IntLiteral(20))],
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_const_declaration_3(self):
        input = """const a = [3]int{10, 20, 30};"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        ArrayLiteral(
                            [IntLiteral(3)],
                            IntType(),
                            [IntLiteral(10), IntLiteral(20), IntLiteral(30)],
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_struct_declaration_1(self):
        input = """type Person struct {
            name string;
            age int;
        };"""
        expect = str(
            Program(
                [StructType("Person", [("name", StringType()), ("age", IntType())], [])]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_struct_declaration_2(self):
        input = """type Person struct {
            name string;
        };"""
        expect = str(Program([StructType("Person", [("name", StringType())], [])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_struct_declaration_3(self):
        input = """type Person struct {
            name string;
            age int;
            address string;
        };"""
        expect = str(
            Program(
                [
                    StructType(
                        "Person",
                        [
                            ("name", StringType()),
                            ("age", IntType()),
                            ("address", StringType()),
                        ],
                        [],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_interface_declaration_1(self):
        input = """type Person interface {
            Hello();
        };"""
        expect = str(
            Program([InterfaceType("Person", [Prototype("Hello", [], VoidType())])])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_interface_declaration_2(self):
        input = """type Person interface {
            Hello();
            Hi() int;
        };"""
        expect = str(
            Program(
                [
                    InterfaceType(
                        "Person",
                        [
                            Prototype("Hello", [], VoidType()),
                            Prototype("Hi", [], IntType()),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_interface_declaration_3(self):
        input = """type Person interface {
            Hello();
            Hi() int;
            Greet(name string);
        };"""
        expect = str(
            Program(
                [
                    InterfaceType(
                        "Person",
                        [
                            Prototype("Hello", [], VoidType()),
                            Prototype("Hi", [], IntType()),
                            Prototype("Greet", [StringType()], VoidType()),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_func_declaration_1(self):
        input = """func main() {
            a := 1;
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main", [], VoidType(), Block([Assign(Id("a"), IntLiteral(1))])
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_func_declaration_2(self):
        input = """func main(a int) {
            a := 1;
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [ParamDecl("a", IntType())],
                        VoidType(),
                        Block([Assign(Id("a"), IntLiteral(1))]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_func_declaration_3(self):
        input = """func main() int {
            return 1;
        };"""
        expect = str(
            Program([FuncDecl("main", [], IntType(), Block([Return(IntLiteral(1))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_func_declaration_4(self):
        input = """func main(a int) int {
            return a;
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [ParamDecl("a", IntType())],
                        IntType(),
                        Block([Return(Id("a"))]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_method_declaration_1(self):
        input = """func (a Person) main() {
            a := 1;
        };"""
        expect = str(
            Program(
                [
                    MethodDecl(
                        "a",
                        Id("Person"),
                        FuncDecl(
                            "main",
                            [],
                            VoidType(),
                            Block([Assign(Id("a"), IntLiteral(1))]),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_method_declaration_2(self):
        input = """func (a Person) main(b int) {
            a := 1;
        };"""
        expect = str(
            Program(
                [
                    MethodDecl(
                        "a",
                        Id("Person"),
                        FuncDecl(
                            "main",
                            [ParamDecl("b", IntType())],
                            VoidType(),
                            Block([Assign(Id("a"), IntLiteral(1))]),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_method_declaration_3(self):
        input = """func (a Person) main() int {
            return 1;
        };"""
        expect = str(
            Program(
                [
                    MethodDecl(
                        "a",
                        Id("Person"),
                        FuncDecl("main", [], IntType(), Block([Return(IntLiteral(1))])),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_method_declaration_4(self):
        input = """func (a Person) main(b int) int {
            return b;
        };"""
        expect = str(
            Program(
                [
                    MethodDecl(
                        "a",
                        Id("Person"),
                        FuncDecl(
                            "main",
                            [ParamDecl("b", IntType())],
                            IntType(),
                            Block([Return(Id("b"))]),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

        #! ------------------ Test Literal ------------------

    def test_integer_literal(self):
        input = """const a = 1;"""
        expect = str(Program([ConstDecl("a", None, IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_negative_integer_literal(self):
        input = """const a = -1;"""
        expect = str(Program([ConstDecl("a", None, UnaryOp("-", IntLiteral(1)))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_boolean_literal(self):
        input = """const a = true;"""
        expect = str(Program([ConstDecl("a", None, BooleanLiteral(True))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_float_literal(self):
        input = """const a = 1.0;"""
        expect = str(Program([ConstDecl("a", None, FloatLiteral(1.0))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_string_literal(self):
        input = """const a = "Hello";"""
        expect = str(Program([ConstDecl("a", None, StringLiteral("Hello"))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_array_literal(self):
        input = """const a = [3]int{10, 20, 30};"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        ArrayLiteral(
                            [IntLiteral(3)],
                            IntType(),
                            [IntLiteral(10), IntLiteral(20), IntLiteral(30)],
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_multi_dimensional_array_literal(self):
        input = """const a = [3][2]int{{1, 2}, {3, 4}, {5, 6}};"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        ArrayLiteral(
                            [IntLiteral(3), IntLiteral(2)],
                            IntType(),
                            [
                                [IntLiteral(1), IntLiteral(2)],
                                [IntLiteral(3), IntLiteral(4)],
                                [IntLiteral(5), IntLiteral(6)],
                            ],
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_struct_literal(self):
        input = """const a = Person{name:"name", age: 20};"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        StructLiteral(
                            "Person",
                            [("name", StringLiteral("name")), ("age", IntLiteral(20))],
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_nil_literal(self):
        input = """const a = nil;"""
        expect = str(Program([ConstDecl("a", None, NilLiteral())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    #! ------------------ Test Expression ------------------
    def test_identifier_expression(self):
        input = """const a = b;"""
        expect = str(Program([ConstDecl("a", None, Id("b"))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_array_element_expression(self):
        input = """const a = b[1];"""
        expect = str(
            Program([ConstDecl("a", None, ArrayCell(Id("b"), [IntLiteral(1)]))])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_array_element_expression_with_expression_index(self):
        input = """const a = b[1 + 2];"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        ArrayCell(
                            Id("b"), [BinaryOp("+", IntLiteral(1), IntLiteral(2))]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_multi_dimensional_array_element_expression(self):
        input = """const a = b[1][2];"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a", None, ArrayCell(Id("b"), [IntLiteral(1), IntLiteral(2)])
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_struct_field_expression(self):
        input = """const a = b.name;"""
        expect = str(Program([ConstDecl("a", None, FieldAccess(Id("b"), "name"))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_nested_struct_field_expression(self):
        input = """const a = b.c.d;"""
        expect = str(
            Program([ConstDecl("a", None, FieldAccess(FieldAccess(Id("b"), "c"), "d"))])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_function_call_expression(self):
        input = """const a = foo();"""
        expect = str(Program([ConstDecl("a", None, FuncCall("foo", []))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_method_call_expression(self):
        input = """const a = b.foo();"""
        expect = str(Program([ConstDecl("a", None, MethCall(Id("b"), "foo", []))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_unary_expression(self):
        input = """const a = -b;"""
        expect = str(Program([ConstDecl("a", None, UnaryOp("-", Id("b")))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_binary_expression(self):
        input = """const a = b + c;"""
        expect = str(Program([ConstDecl("a", None, BinaryOp("+", Id("b"), Id("c")))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_large_expression(self):
        input = """const a = b + c * d / e % f;"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        BinaryOp(
                            "+",
                            Id("b"),
                            BinaryOp(
                                "%",
                                BinaryOp("/", BinaryOp("*", Id("c"), Id("d")), Id("e")),
                                Id("f"),
                            ),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_expression_with_parentheses(self):
        input = """const a = (b + c) * d;"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        BinaryOp("*", BinaryOp("+", Id("b"), Id("c")), Id("d")),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_logical_expression(self):
        input = """const a = b && c || d && !e;"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        BinaryOp(
                            "||",
                            BinaryOp("&&", Id("b"), Id("c")),
                            BinaryOp("&&", Id("d"), UnaryOp("!", Id("e"))),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    #! ------------------ Test Program ------------------
    def test_program_1(self):
        input = """func main() {
                say("Hello, world!");
            };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block([FuncCall("say", [StringLiteral("Hello, world!")])]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_program_2(self):
        input = """func foo () {
            a := 1;
            b := 2;
            return a + b;
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "foo",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(Id("a"), IntLiteral(1)),
                                Assign(Id("b"), IntLiteral(2)),
                                Return(BinaryOp("+", Id("a"), Id("b"))),
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_program_3(self):
        input = """var a int;"""
        expect = str(Program([VarDecl("a", IntType(), None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_program_4(self):
        input = """type a struct {
            name string;
            };"""
        expect = str(Program([StructType("a", [("name", StringType())], [])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_program_5(self):
        input = """func main() {
            a := 1;
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main", [], VoidType(), Block([Assign(Id("a"), IntLiteral(1))])
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    #! ------------------ Test Statement ------------------
    def test_var_declaration_statement(self):
        input = """func main() {var a int;};"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main", [], VoidType(), Block([VarDecl("a", IntType(), None)])
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_const_declaration_statement(self):
        input = """func main() {const a = 1;};"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block([ConstDecl("a", None, IntLiteral(1))]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_assignment_statement(self):
        input = """func main() {a := 1;};"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main", [], VoidType(), Block([Assign(Id("a"), IntLiteral(1))])
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_assignment_statement_with_expression(self):
        input = """func main() {a := b + c;};"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block([Assign(Id("a"), BinaryOp("+", Id("b"), Id("c")))]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_assignment_statement_with_operator(self):
        input = """func main() {a += b;};"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block([Assign(Id("a"), BinaryOp("+", Id("a"), Id("b")))]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_if_statement(self):
        input = """func main() {
            if (a == 1) {a := 10;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp("==", Id("a"), IntLiteral(1)),
                                    Block([Assign(Id("a"), IntLiteral(10))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_if_else_statement(self):
        input = """func main() {if (a == 1) {a := 10;} else {a := 20;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp("==", Id("a"), IntLiteral(1)),
                                    Block([Assign(Id("a"), IntLiteral(10))]),
                                    Block([Assign(Id("a"), IntLiteral(20))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_if_else_if_statement(self):
        input = """func main() {if (a == 1) {a := 10;} else if (a >= 1) {a := 20;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp("==", Id("a"), IntLiteral(1)),
                                    Block([Assign(Id("a"), IntLiteral(10))]),
                                    If(
                                        BinaryOp(">=", Id("a"), IntLiteral(1)),
                                        Block([Assign(Id("a"), IntLiteral(20))]),
                                        None,
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_for_statement(self):
        input = """func main() {for i < 10 {a := i;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForBasic(
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Block([Assign(Id("a"), Id("i"))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_for_loop_statement(self):
        input = """func main() {for i := 0; i < 10; i+=1 {a := i;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(
                                        Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))
                                    ),
                                    Block([Assign(Id("a"), Id("i"))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_for_range_statement(self):
        input = """func main() {for i, value := range a {a := value;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForEach(
                                    Id("i"),
                                    Id("value"),
                                    Id("a"),
                                    Block([Assign(Id("a"), Id("value"))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_break_statement(self):
        input = """func main() {break;};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_continue_statement(self):
        input = """func main() {continue;};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_return_statement(self):
        input = """func main() {return 1;};"""
        expect = str(
            Program([FuncDecl("main", [], VoidType(), Block([Return(IntLiteral(1))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_return_statement_without_expression(self):
        input = """func main() {return;};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_call_statement(self):
        input = """func main() {foo();};"""
        expect = str(
            Program([FuncDecl("main", [], VoidType(), Block([FuncCall("foo", [])]))])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_call_statement_with_parameter(self):
        input = """func main() {foo(a);};"""
        expect = str(
            Program(
                [FuncDecl("main", [], VoidType(), Block([FuncCall("foo", [Id("a")])]))]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_method_call_statement(self):
        input = """func main() {a.foo();};"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main", [], VoidType(), Block([MethCall(Id("a"), "foo", [])])
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_method_call_statement_with_parameter(self):
        input = """func main() {a.foo(b);};"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block([MethCall(Id("a"), "foo", [Id("b")])]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_if_statement_with_return(self):
        input = """func main() {if (a == 1) {return 1;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp("==", Id("a"), IntLiteral(1)),
                                    Block([Return(IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_if_statement_with_break_and_continue(self):
        input = """func main() {if (a == 1) {break;} else {continue;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp("==", Id("a"), IntLiteral(1)),
                                    Block([Break()]),
                                    Block([Continue()]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_for_statement_with_return(self):
        input = """func main() {for i < 10 {return i;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForBasic(
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Block([Return(Id("i"))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_for_loop_statement_with_break(self):
        input = """func main() {for i := 0; i < 10; i+=1 {break;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(
                                        Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))
                                    ),
                                    Block([Break()]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_for_range_statement_with_continue(self):
        input = """func main() {for i, value := range a {continue;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForEach(
                                    Id("i"), Id("value"), Id("a"), Block([Continue()])
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_nested_if_statement(self):
        input = """func main() {
            if (a == 1) {
                if (b > 2) {a := 10;}
            }
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp("==", Id("a"), IntLiteral(1)),
                                    Block(
                                        [
                                            If(
                                                BinaryOp(">", Id("b"), IntLiteral(2)),
                                                Block(
                                                    [Assign(Id("a"), IntLiteral(10))]
                                                ),
                                                None,
                                            )
                                        ]
                                    ),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_nested_for_statement(self):
        input = """func main() {for i < 10 {for j := 0; j < 5; j+=1 {a := i + j;}
        }
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForBasic(
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Block(
                                        [
                                            ForStep(
                                                Assign(Id("j"), IntLiteral(0)),
                                                BinaryOp("<", Id("j"), IntLiteral(5)),
                                                Assign(
                                                    Id("j"),
                                                    BinaryOp(
                                                        "+", Id("j"), IntLiteral(1)
                                                    ),
                                                ),
                                                Block(
                                                    [
                                                        Assign(
                                                            Id("a"),
                                                            BinaryOp(
                                                                "+", Id("i"), Id("j")
                                                            ),
                                                        )
                                                    ]
                                                ),
                                            )
                                        ]
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_if_statement_with_call_statement(self):
        input = """func main() {if (a == 1) {foo();}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp("==", Id("a"), IntLiteral(1)),
                                    Block([FuncCall("foo", [])]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_for_statement_with_return_statement(self):
        input = """func main() {for i < 10 {return i;}
        };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForBasic(
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Block([Return(Id("i"))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_multiple_statements_in_block(self):
        input = """func main() {a := 1; b := 2; return a + b;};"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(Id("a"), IntLiteral(1)),
                                Assign(Id("b"), IntLiteral(2)),
                                Return(BinaryOp("+", Id("a"), Id("b"))),
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    #! ------------------ Advance ------------------
    def test_integer_octal_literal(self):
        input = """const a = 0o123;"""
        expect = str(Program([ConstDecl("a", None, IntLiteral(83))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_integer_hex_literal(self):
        input = """const a = 0x123;"""
        expect = str(Program([ConstDecl("a", None, IntLiteral(291))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_float_literal_with_exponent(self):
        input = """const a = 1.0e-2;"""
        expect = str(Program([ConstDecl("a", None, FloatLiteral(0.01))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_integer_binary_literal(self):
        input = """const a = 0b101;"""
        expect = str(Program([ConstDecl("a", None, IntLiteral(5))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_expression_with_same_precedence(self):
        input = """const a = 1 + 2 - 3;"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        BinaryOp(
                            "-",
                            BinaryOp("+", IntLiteral(1), IntLiteral(2)),
                            IntLiteral(3),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_expression_with_same_precedence_2(self):
        input = """const a = 1 * 2 / 3;"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        BinaryOp(
                            "/",
                            BinaryOp("*", IntLiteral(1), IntLiteral(2)),
                            IntLiteral(3),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_expression_with_same_precedence_3(self):
        input = """const a = 1 * 2 % 3;"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        BinaryOp(
                            "%",
                            BinaryOp("*", IntLiteral(1), IntLiteral(2)),
                            IntLiteral(3),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_expression_with_same_precedence_4(self):
        input = """const a = x.y[z];"""
        expect = str(
            Program(
                [ConstDecl("a", None, ArrayCell(FieldAccess(Id("x"), "y"), [Id("z")]))]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_unary_expression(self):
        input = """const a = -b + c;"""
        expect = str(
            Program(
                [
                    ConstDecl(
                        "a",
                        None,
                        BinaryOp("+", UnaryOp("-", Id("b")), Id("c")),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_unary_expression_2(self):
        """Expression with ! and -"""
        input = """const a = !-b;"""
        expect = str(Program([ConstDecl("a", None, UnaryOp("!", UnaryOp("-", Id("b"))))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))