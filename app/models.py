class Sources:
    '''
    Source class that defines source objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class Top_Headlines:
    '''
    Top headlines class that defines top headlines objects
    '''
    def __init__(self, author, title, description, url, urlToImage, publishedAt, content):
        self.author = author
        self.title = title
        self.publishedAt = publishedAt
        self.content = content
        self.urlToImage = urlToImage
        self.url = url
        self.description = description

class Everything :
    '''
    Everything class that defines everything objects
    '''
    def __init__(self, author, title, description, url, urlToImage, publishedAt, content):
        self.author = author
        self.title = title
        self.publishedAt = publishedAt
        self.content = content
        self.urlToImage = urlToImage
        self.url = url
        self.description = description