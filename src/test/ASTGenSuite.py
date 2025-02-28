import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

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
        self.assertTrue(TestAST.checkASTGen(input, expect, 201))

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
        self.assertTrue(TestAST.checkASTGen(input, expect, 202))

    def test_program_3(self):
        input = """var a int;"""
        expect = str(Program([VarDecl("a", IntType(), None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 203))

    def test_program_4(self):
        input = """type a struct {
            name string;
            };"""
        expect = str(Program([StructType("a", [("name", StringType())], [])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 204))

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
        self.assertTrue(TestAST.checkASTGen(input, expect, 205))

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
