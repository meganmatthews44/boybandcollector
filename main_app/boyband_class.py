class Boyband:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, decade, albums_sold, no_of_members):
    self.name = name
    self.decade = decade
    self.albums_sold = albums_sold
    self.no_of_members = no_of_members

boybands = [
  Boyband('Backstreet Boys', '1990s', 'MILLIONS', 5),
  Boyband('NKOTB', '1980s', 'MILLIONS', 5),
  Boyband('*NSync', '1990s', 'Thousands', 5)
]