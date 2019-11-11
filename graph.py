import matplotlib.pyplot as plt

year = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
pop_twitter_use = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6, 7, 8, 9, 10, 2, 3, 4, 0]
pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1, 7, 8, 9, 10, 2, 3, 4, 0]
plt.plot(year, pop_twitter_use, color='blue')
plt.plot(year, pop_india, color='violet')
plt.xlabel('Year')
plt.ylabel('Occurences')
plt.title('How much has your hashtag been used?')
plt.show()