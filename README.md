
![](https://github.com/bonghoa15/ReadabilityLola/blob/master/banner_bonghoa.jpg)

<code> <i>INSTALLATION</i> 
```Pip install readabilitylola ```

The goal of this repo is to implement readability score of local languages including: Bahasa, Hindi
1.	Readability 
Is the quality of your writing. If the readability of your text is high, people will be able to understand your sentences easily. If the readability is low, people still might understand what you are saying, but it is likely to be a draining experience. Instead of skimming quickly over your writing, reader needs to spend significant amount of energy unpacking big vocabulary and complex sentence structure. Briefly, It demands more concentration from your reader. 
2.	Readability score
A computer-calculated index which can tell how easy it will be for someone to read a particular piece of text. Readability score is well defined in English language for a long time. However, there is little research for other languages. Also, some popular formula of computing readability score in English is not suitable in other language. So far, I have found the score is researched for Bahasa, Hindi. <br />

================ <br />
Bahasa readability score formula: 
```$$\-13.988 + 0.3793(300/S) + 0.0207(d+ k)$$ ```


Where: <br />
S: number of sentence in 300 words <br />
d: number of syllables <br />
k: potentiall difficullt words including Kata Ganda,Diftong, Kata Pinjaman and Kekeliruan huruf. Specifically k= 5*(Kata Ganda+Diftong+Kata Pinjaman+Kekeliruan Huruf) <br />
================ <br />
Hindi readability score formula: 
```$$\-2.34+2.14AWL+0.01PSW $$ ```

Where: <br />
AWL: average word length <br />
PSW: Poly-syllabic words are the words whose count of syllable exceeds 2





