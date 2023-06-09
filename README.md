## Overview

This is a command line application for performing "queer distant reading" of literary text inspired by Judith Butler's theory of Gender Performativity.

The goal of the tool is to enable a praxis for studying text (such as gender terms "woman" and "man") that self-consciously takes the workings of technology and applies them within a gender theory frame.

This project is *very much* in progress, and I welcome any suggestions! Thank you.

## Theoretical Framework

There are two aspects of Butler's theory of Gender Performativity that influenced the development of this text-analysis tool.

First, that gender is active. It is a series of actions, like a habit, as Butler defines in her famous book, Gender Trouble:

```console 
"Gender is the repeated stylization of the body, a set of repeated acts within a highly rigid, regulatory frame that congeal over time to produce the appearance of a substance, of a natural sort of being" (Gender Trouble 33). 
```

Second, that these series of actions are productive, in two ways. They produce the subject, bring the subject into being, rather than represent an expression of the subject or of a pre-existing subjectivity. This is an important point that Butler makes in her followup book, Bodies that Matter: on the Discursive Limits of Sex (1996), when she says "There is no power that acts, but only a reiterated acting that is power in its persistence and instability" (Bodies xviii). The second productive aspect has to do with language. Here, Butler makes a major claim about language producing reality, rather than referencing it:

```console
"The mimetic or representational status of language…. is not mimetic at all. On the contrary, it is productive, constitutive, one might even argue performative" (Bodies 6). 
```

This point, that language produces the reality that it seems to merely reference, opens a possibility for re-signifying the meaning of certain terms. Butler offers the famous example in the resignification of the term "queer," which has been transformed from a term of abjection to one of empowerment. "Queer" achieves this resignification by harnessing its own abjection which is repudiated in every identification with heterosexuality. Because performativity produces meaning, therein lies the possibility of resistance, the possibility of resignifying meaning. 

## Usage

First, download the project to your own computer. 

Then, using a command-line program of your choice, navigate to the folder just above the downloaded folder. 

To run the program, input a command that contains 4 arguments. 

The first argument is the  `python` command and the second argument is the module name `qdr`

The last two arguments are customizable. The third argument specifies a text to analyze like `orlando.txt` (which comes packaged with the app) and the term that you want to analyze, in this case, `woman`.

```console
% python qdr orlando.txt woman
```

The results of this code will give us a list of similar words, that is, words which appear next to or nearby our search term `woman`. It will give us a list of terms in the format of a "word embedding" 

```console
% python qdr orlando.txt woman
[('fling', 0.38121166825294495),
 ('abase', 0.35150107741355896),
 ('flower', 0.33490291237831116),
 ('superior', 0.3274153470993042),
 ('witticism', 0.3148716390132904),
 ('fight', 0.313768208026886),
 ('coal', 0.308252215385437),
 ('impassable', 0.3044101893901825),
 ('unenticed', 0.3026406466960907),
 ('tavern', 0.3014964759349823)]
```

Word embeddings, also known as "vectors," are essentially a list of words that are associated with the search term. 
The score that appears next to each word in the results represents a probability of how often that word appears nearby the search term. To learn more, check out this [excellent explanation of word embeddings](https://jalammar.github.io/illustrated-word2vec/) (from a Machine Learning perspective) from Jay Alammar.

Besides searching for similar words (and obtaining word embeddings), we can also use the tool to see specific words in context. To do this, Add the `-c` tag to the command line arguments. The results will list the search word within a "context window," that is, the words immediately preceding and immediately following the search term.

```console
% python qdr orlando.txt woman -c
and manly charm -- all qualities which the old woman loved the more the more they failed her . For 
d up and dyed her cheeks scarlet . For the old woman loved him . And the Queen , who knew a man whe
tumn , overladen with apples . The old bumboat woman , who was carrying her fruit to market on the 
Embassy , a figure , which , whether boy 's or woman 's , for the loose tunic and trousers of the R
en the boy , for alas , a boy it must be -- no woman could skate with such speed and vigour -- swep
...
```

## Try it!

Go to this [Google Colab document](https://colab.research.google.com/drive/18onAnrf8Qrf0b3rm3XMCPHaDy152PjoS?usp=sharing), make a copy of the document (File > Save a copy in Drive), and run the code in the cells. 





