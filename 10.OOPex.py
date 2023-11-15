#These exercises cover fundamental aspects of OOP, encapsulation, 
#inheritance (not explicitly used but could be extended), and composition. 
#They also involve the use of methods, attributes, and basic control structures in Python.

### Ushtrimi 1 ###
# Krijoni nje klas Rectangle qe na mundeson metoda
# per llogaritjen e siperfaqes dhe perimetrit


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length


# rectangle_1 = Rectangle(10, 20)
# print(rectangle_1.perimeter())
# print(rectangle_1.area())


### Ushtrimi 2 ###
# krijoni nje class Library qe na mundeson shtimin e nje libri,
# fshirjen e nje libri dhe gjetjen e nje ose dis librave
# sipas nje pjese te titullit


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        if title not in self.books:
            self.books.append(title)
            print(f"Libri {title} u shtua ne librari!")

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print(f"Libri {title} u hoq nga libraria!")
        else:
            print(f"Nuk ekzsiston nje liber me titullin {title}!")

    def search_book(self, partial_title):
        result_list = []
        for book in self.books:
            if partial_title in book:
                result_list.append(book)
        if not result_list:
            print(f"Nuk u gjet asnje liber qe permban {partial_title}!")
        return result_list


# my_library = Library()
# my_library.add_book("Harry Potter 1")
# my_library.add_book("Harry Potter 2")
# my_library.add_book("Harry Potter 3")
# my_library.add_book("Fantastic Beasts 1")


# my_library.remove_book("Fantastic Beasts 2")
# my_library.remove_book("Harry Potter 2")
# my_library.remove_book("Harry Potter")


# print(my_library.search_book("Harry Potter"))

# print(my_library.books)


### Ushtrimi 3 ###
# krijoni nje klase BankAccount e cila mundeson transferta parash
# nga nje objekt i kesaj klase ne nje objekt tjeter.
# gjithashtu cdo llogari do kete nje account_id, i cili do rritet
# me 1 per cdo objekt te krijuar


class BankAccount:
    GLOBAL_ID = 0

    def __init__(self, balance):
        BankAccount.GLOBAL_ID += 1
        self.account_id = BankAccount.GLOBAL_ID
        self.balance = balance

    def transfer(self, receiver_account, amount):
        if self.balance < amount:
            print("Nuk ka mjaftueshem balanc!")
        else:
            receiver_account.balance += amount
            self.balance -= amount
            print("Transferta u krye!")


# bank_account_1 = BankAccount(100)
# bank_account_2 = BankAccount(20)
# print(bank_account_1.account_id)
# print(bank_account_2.account_id)

# bank_account_1.transfer(bank_account_2, 120)

# print(bank_account_1.balance)
# print(bank_account_2.balance)


### Ushtrimi 4 ###
# krjoni 2 klasa, PlayList dhe Song
# Song do kete emrin e autorit, emrin e kenges, kohezgjatjen e kenges ne sekonda
# PlayList do permbaj disa Song, do kete nje metod shuffle qe ndryshon
# radhen e ketyre Songs, do mundesoj llogaritjen e kohezgjatjes se kesaj PlayList,
# do mundesoj gjetjen e te gjithe autoreve qe ndodhen ne kete PlayList

from random import shuffle


class Song:
    def __init__(self, author, name, duration):
        self.author = author
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"Author: {self.author}, Title: {self.name}"

    def __repr__(self):
        return f"Author: {self.author}, Title: {self.name}"


class PlayList:
    def __init__(self, songs: list[Song]):
        self.songs = songs

    def add_song(self, song: Song):
        if song not in self.songs:
            self.songs.append(song)

    def remove_song(self, song: Song):
        if song in self.songs:
            self.songs.remove(song)

    def shuffle_songs(self) -> list[Song]:
        shuffle(self.songs)  # changes the order of the objects in the list self.songs

    def playlist_duration(self) -> int:
        duration = 0
        for song in self.songs:
            duration += song.duration
        return duration

    def playlist_authors(self) -> list[str]:
        authors_list = []
        for song in self.songs:
            if song.author not in authors_list:
                authors_list.append(song.author)
        return authors_list
        # return list(set([song.author for song in self.songs]))

    def __add__(
        self, other_playlist
    ):  # defines what happens when we add 2 objects of the PlayList class
        return self.songs + other_playlist.songs

    def __lt__(
        self, other_playlist
    ):  # defines what happens when we compare with '<' 2 objects of the PlayList class
        return self.playlist_duration() <= other_playlist.playlist_duration()


# song_1 = Song("Noizy", "Jena Mbreter", 180)
# song_2 = Song("Noizy", "Jena Mbreter 2", 200)
# song_3 = Song("Varrosi", "Shqipet Ka Londra", 180)
# song_4 = Song("Fatmira Brecani", "Xinxilushe", 200)

# playlist_1 = PlayList([song_1, song_2, song_3])
# playlist_2 = PlayList([song_4])


# print(playlist_1 < playlist_2)


# playlist_1.shuffle_songs()
# # print(playlist_1.songs)

# print(playlist_1.playlist_duration())
# print(playlist_1.playlist_authors())


### Ushtrimi 5 ###
# Krijoni nje klas SocialNetwork, nje klas Post dhe nje klas User
# klasa SocialNetwork:
#   - get all regsitered users
#   - get all posts
# klasa Post:
#   - get number of likes
#   - get list of users that liked the post
#   - get the user that created the post
# klasa user:
#   - a user can create a post
#   - a user can like a post
#   - a user can unlike a post (only if he liked it before)
#   - the user that created the post can delete it and modify it


class SocialNetwork:
    def __init__(self):
        self.posts = []
        self.users = []

    def get_posts(self):
        return self.posts

    def get_users(self):
        return self.users


class Post:
    def __init__(self, content, user):
        self.content = content
        self.author = user
        self.list_of_likes = []

    def number_of_likes(self):
        return len(self.list_of_likes)

    def users_liked_the_post(self):
        return self.list_of_likes

    def get_author(self):
        return self.author


class User:
    def __init__(self, username, social_network):
        self.username = username
        self.social_network = social_network

    def like(self, post):
        if self not in post.list_of_likes:
            post.list_of_likes.append(self)
            print("Post liked!")
        else:
            print("You have already liked this post!")

    def unlike(self, post):
        if self in post.list_of_likes:
            post.list_of_likes.remove(self)
            print("Post unliked!")
        else:
            print("You cannot unlike a post that you have not liked before!")

    def create_post(self, content):
        post = Post(content, self)
        self.social_network.posts.append(post)
        print("Post created!")
        return post

    def delete_post(self, post):
        if post.author == self:
            self.social_network.posts.remove(post)
        else:
            print("You are not the post author! You cannot delete it!")

    def edit_post(self, post, new_content):
        if post.author == self:
            post.content = new_content
        else:
            print("You are not the post author! You cannot edit it!")
