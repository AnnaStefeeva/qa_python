# qa_python

### 1. test_add_new_book_add_two_books
Тест проверяет добавление в словарь двух книг
### 2. test_add_new_book_with_name_between_1_and_40_characters
Тест проверяет, что в словарь можно добавить книгу с названием длиной от 1 до 40 символов
### 3. test_add_new_book_with_name_0_and_41_characters
Тест проверяет, что в словарь нельзя добавить книгу с названием длиной 1 символ и длиной 41 символ
### 4. test_add_new_book_add_the_same_book_twice
Тест проверяет, что одну и ту же книгу можно добавить в словарь только один раз
### 5. test_set_book_genre_set_book_correct_genre
Тест проверяет, что книге устанавливается жанр из списка genre
### 6. test_set_book_genre_set_book_incorrect_genre
Тест проверяет, что книге не будет установлен жанр, если он не входит в список genre
### 7. test_get_book_genre_get_genre_for_incorrect_book
Тест проверяет, что книге, которой нет в словаре books_genre, жанр не будет выведен 
### 8. test_get_books_with_specific_genre_get_genre_for_two_books
Тест проверяет добавление 2 книг, присвоение этим книгам жанра, а также выводит списки определенных жанров, включающих новые книги 
### 9. test_add_book_in_favorites_add_in_favorites_one_book
Тест проверяет добавление в список избранного одной книги
### 10. test_delete_book_from_favorites_delete_1_book_from_favorites
Тест проверяет удаление одной книги из списка избранного
### 11. test_get_books_for_children_get_3_books_for_children
Тест проверяет добавление 5 книг, присвоение им жанров, выделение из этих 5 книг 3 книг с жанрами, подходящими для детей    
### 12. test_get_books_genre_get_books_genre_of_1_book
Тест проверяет, что одна добавленная книга выводится в текущем словаре books_genre.
### 13. test_get_list_of_favorites_books_get_2_favorites_books 
Тест проверяет, что список избранного содержит 2 книги
