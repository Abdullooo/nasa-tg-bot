интересные_текст = {1: "The James Webb telescope has been under construction for a quarter of a century.",
                    2: "Initially, only $500 million was planned for its construction. The telescope itself was invested 9.7 billion dollars, but from the side of NASA, ESA invested 700 million euros in it, Canada invested 200 million Canadian dollars in it, for a total of 10.500.000.000 dollars.",
                    3: "The project was made not only by America, Europe and Canada took part from there, in total 17 countries of the world took part in it.",
                    4: "This telescope is the largest telescope in the world, its dimensions are 20.2 x 14.2 m.",
                    5: "His mirrors are covered with a thin layer of gold, which is why they are yellow.",
                    6: "Initially, the launch was supposed to be in 2010, then 2016, but then another 5 years were added to it, some humorists from God came up with their own decoding due to frequent transfers, Just Wait Space Telescope.",
                    7: "It is located at a distance of 1.5 million kilometers from Earth.",
                    8: "Its honeycomb-like mirrors are segments of the primary mirror of a new infrared space telescope. Its mirrors are the size of a man.",
                    9: "The weight of one telescope mirror is 6161.42 kg.",
                    10: "Initially, the telescope was called NGST (New Generations Space Telescope - New Generation Space Telescope).",
                    11: "The telescope was named James Webb in honor of the head of NASA, James Webb, the former head of NASA from 1961-1968.",
                    12: "The current name of the Just Wonderful Space Telescope is the Just Wonderful Space Telescope."}

интересные_фото = {1: "https://rg.ru/uploads/images/223/46/03/111.jpg",
                   2: "https://thumbs.dreamstime.com/b/%D0%BC%D0%BE%D1%80%D0%B5-%D0%BD%D0%B0-%D0%B8%D1%87%D0%BD%D1%8B%D1%85-%D0%B5%D0%BD%D0%B5%D0%B3-52649810.jpg",
                   3: "https://image.shutterstock.com/image-illustration/canada-usa-america-european-union-260nw-1314885344.jpg",
                   4: "https://hi-news.ru/wp-content/uploads/2015/10/JWST_people.jpg",
                   5: "https://skyandtelescope.org/wp-content/uploads/james_webb_space_telescope-600x400.jpg",
                   6: "https://knowhow.pp.ua/wp-content/uploads/2021/12/new-lead-4.jpg",
                   7: "https://scx1.b-cdn.net/csz/news/800a/2022/james-webb-space-teles-2.jpg",
                   8: "https://cdn.segodnya.ua/media/image/61c/713/893/61c713893c87f.jpeg",
                   9: "https://elementy.ru/images/kartinka_dnya/jwst_picture_of_the_day_1_650.jpg",
                   10: "https://3dnews.ru/assets/external/illustrations/2021/09/08/1048614/gHnTKJuEt8f6QR.jpg",
                   11: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/James_E._Webb%2C_official_NASA_photo%2C_1966.jpg/240px-James_E._Webb%2C_official_NASA_photo%2C_1966.jpg",
                   12: "https://cdnn21.img.ria.ru/images/19067/40/190674013_0:15:1050:610_600x0_80_0_0_a19ba7d57a4efc54785b6028accb1581.jpg"}

poll_question = "Guess which of these pictures was taken by the James Webb satellite"

poll_photos = {
    1: "https://tayna24.ru/wp-content/uploads/2022/07/1657878833_997_sravnivaja-izobrazhenija-habbla-i-dzhejmsa-ujebba-rjadom-curiosmos.png",#2
    2: "https://sm.mashable.com/mashable_in/photo/default/image-8_7j72.jpg",#1
    3: "https://i.insider.com/62cd33b3114c1e0018731e58?format=jpeg",#2
    4: "https://ic-cdn.flipboard.com/s-nbcnews.com/1f30590dd51a3b80fad0e636eb15ad25c8ae7f80/_large.jpeg",#2
    5: "https://media.npr.org/assets/img/2021/09/13/heic1406c_wide-0b0f0abe0f7827f76e9e3daa017c898448a83045.jpg?s=1400",#1
    6: "https://hightech.fm/wp-content/uploads/2022/09/snimok-jekrana-2022-09-27-145406-1.jpg",#1
    7: "https://www.pvsm.ru/images/2021/09/29/samyi-bolshoi-kosmicheskii-teleskop-djeims-uebb-doljen-izmenit-nashi-predstavleniya-o-kosmose-5.jpeg",#2
    8: "https://www.ixbt.com/img/n1/news/2021/6/2/stsci-01faxk0ed0mvrj76p55cbb66rh_large.png",#2
    9: "https://danielmarin.naukas.com/files/2022/07/FXa-HlIXoAcV8An-scaled.jpeg",#2
    10: "https://cdn.telegram-site.com/images/1/1/6/4/7/3/1/2/5/5/e1379d17ec84841f5137b82641fb3841.jpg"}#2


polls = {

}


class Poll:
    question: str
    photo_url: str
    win_option: int  # 0 - left, 1 - right

    def __init__(self, question: str, photo_url: str, win_option: int):
        self.question = question
        self.photo_url = photo_url
        self.win_option = win_option


for i in range(1, len(poll_photos.keys())):

    question = poll_question
    photo_url = poll_photos[i]

    if i in [2, 5, 6]:
        win_option = 1
    else:
        win_option = 2

    poll = Poll(
        question, photo_url, win_option
    )

    polls[i] = poll