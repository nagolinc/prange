prange
====

Generate a progress bar (based off of tqdm), but with amusing text to go along with it.


For example

```
|########--| 81/100  81% [elapsed: 01:21 left: 00:19,  1.00 iters/sec]
You happen upon a fight betwen a Portuguese man o' war and an African leopard!
```

The text is generated using a simplified language that allows you to:
1) Randomly choose between different sentences
2) Randomly fill in bits of sentences

A bit of a specialized markup for this looks like

```

animal
  lion
  tiger
  bear
  
event
  You see [animal.aAn]
  
```

This would generate sentences like "You see a bear"

currently only limited grammar is implemented.  You can add ".aAn" to a word to prefix it
with an appropriate choice of "a" or "an" and you can add ".plural" to convert something
to plural (add "s", "es" or "ies" as appropriate).

---

Thanks:

The code for generating the progress bar is from tqdm (https://github.com/noamraph/tqdm)


---

Lisence,

All code is yours to use, modify and share under the MIT License






























