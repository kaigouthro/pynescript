import pyparsing

debug = False

if debug:
    pyparsing.enable_all_warnings()
    pyparsing.enable_diag(pyparsing.Diagnostics.enable_debug_on_named_expressions)
    pyparsing.disable_diag(
        pyparsing.Diagnostics.warn_ungrouped_named_tokens_in_collection
    )

pyparsing.ParserElement.enable_left_recursion()

from . import assignment as assignment_grammars
from . import common as common_grammars
from . import expression as expression_grammars
from . import module as module_grammars
from . import statement as statement_grammars
from . import structure as structure_grammars
from . import library as library_grammars
from . import user_defined_types as user_defined_types_grammars
from . import methods as methods_grammars
from . import maps as maps_grammars

# Add code here to update the parsers for libraries
# Add code here to update the lexers for libraries
# Add code here to update the types for libraries

# Add code here to update the parsers for user-defined types
# Add code here to update the lexers for user-defined types
# Add code here to update the types for user-defined types

# Add code here to update the parsers for methods
# Add code here to update the lexers for methods
# Add code here to update the types for methods

# Add code here to update the parsers for maps
# Add code here to update the lexers for maps
# Add code here to update the types for maps

common_grammars.expression <<= expression_grammars.expression
common_grammars.local_statement <<= statement_grammars.local_statement

expression_grammars.attributed_name <<= common_grammars.attributed_name
expression_grammars.function_call <<= common_grammars.function_call
expression_grammars.structure <<= structure_grammars.structure

structure_grammars.expression <<= expression_grammars.expression
structure_grammars.local_block <<= common_grammars.local_block
structure_grammars.local_body <<= common_grammars.local_body
structure_grammars.identifier_declarator <<= common_grammars.identifier_declarator
structure_grammars.declarator <<= common_grammars.declarator

assignment_grammars.expression <<= expression_grammars.expression
assignment_grammars.type_specifier <<= common_grammars.type_specifier
assignment_grammars.identifier_declarator <<= common_grammars.identifier_declarator
assignment_grammars.tuple_declarator <<= common_grammars.tuple_declarator

statement_grammars.assignment <<= assignment_grammars.assignment
statement_grammars.expression <<= expression_grammars.expression
statement_grammars.local_body <<= common_grammars.local_body

module_grammars.global_statement <<= statement_grammars.global_statement

pyparsing.autoname_elements()

from .assignment import *
from .common import *
from .expression import *
from .module import *
from .statement import *
from .structure import *
from .library import *
from .user_defined_types import *
from .methods import *
from .maps import *