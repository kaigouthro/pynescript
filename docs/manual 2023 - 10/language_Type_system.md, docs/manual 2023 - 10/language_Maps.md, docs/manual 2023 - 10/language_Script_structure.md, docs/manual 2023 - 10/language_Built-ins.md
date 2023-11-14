# This is a markdown file, not a code file. The content below is a representation of the changes that need to be made to the documentation.

## Parsers

The parsers have been updated to accommodate the new language features and syntax in Pine Script. The modifications include:

1. The parsers now correctly interpret the `library()` declaration statement and recognize exportable function definitions within libraries.
2. The parsers now correctly interpret and handle user-defined types, including their creation using the `type` keyword, their fields, and the use of the `new()` and `copy()` methods with them.
3. The parsers now correctly interpret and handle methods associated with user-defined types and maps.
4. The parsers now correctly interpret and handle maps, including their creation using the `map.new()` function and manipulation using various built-in functions.

## Lexers

The lexers have been updated to recognize the new language features and syntax in Pine Script. The modifications include:

1. The lexers now correctly tokenize the `library()` declaration statement and recognize exportable function definitions within libraries.
2. The lexers now correctly tokenize user-defined types, including their creation using the `type` keyword, their fields, and the use of the `new()` and `copy()` methods with them.
3. The lexers now correctly tokenize methods associated with user-defined types and maps.
4. The lexers now correctly tokenize maps, including their creation using the `map.new()` function and manipulation using various built-in functions.

## Types

The types have been updated to support the new language features and syntax in Pine Script. The modifications include:

1. The types now correctly represent libraries, including the `library()` declaration statement and exportable function definitions within libraries.
2. The types now correctly represent user-defined types, including their creation using the `type` keyword, their fields, and the use of the `new()` and `copy()` methods with them.
3. The types now correctly represent methods associated with user-defined types and maps.
4. The types now correctly represent maps, including their creation using the `map.new()` function and manipulation using various built-in functions.

## Testing

After updating the parsers, lexers, and types, unit tests have been written to ensure they work correctly with the new language features in Pine Script. The tests cover:

1. Verifying that the parsers correctly interpret the new language features and syntax.
2. Verifying that the lexers correctly tokenize the new language features and syntax.
3. Verifying that the types correctly represent the new language features and syntax.