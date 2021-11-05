from ZillowScrapper import ZillowScraper

scraper = ZillowScraper("https://www.zillow.com/grand-rapids-mi/rentals/1-_beds/?searchQueryState=%7B%22pagination%22"
                        "%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Grand%20Rapids%2C%20MI%22%2C%22mapBounds%22%3A%7B"
                        "%22west%22%3A-85.7886544243164%2C%22east%22%3A-85.3656807915039%2C%22south%22%3A42"
                        ".80224935930794%2C%22north%22%3A43.067680623666675%7D%2C%22mapZoom%22%3A11%2C"
                        "%22regionSelection%22%3A%5B%7B%22regionId%22%3A11671%2C%22regionType%22%3A6%7D%5D%2C"
                        "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max"
                        "%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D"
                        "%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000"
                        "%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22"
                        "%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B"
                        "%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22"
                        "%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D")

scraper.get_all_the_pages()
