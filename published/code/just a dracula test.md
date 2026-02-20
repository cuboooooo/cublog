

lets see if my custom theme works lol 
(it probably wont and i have 2 exams today so its not getting fixed until next week lmao)

```css
/* Pink - White */
body {
  /* Cyan - Pink - Purple */
  background: #000;
}

/* Green - White */
#dracula {
  display: none;
  visibility: hidden;
  height: calc(var(--deathDate) - var(--birthDate));
  /* Cyan - Pink - Yellow (string) */
  font-family: "Transylvania";
  /* Cyan - Pink - Purple */
  opacity: 0;
}

```

ooh css

```js
/*
 * Once upon a time...
 */
class Vampire {
  constructor(props) {
    this.location = props.location;
    this.birthDate = props.birthDate;
    this.deathDate = props.deathDate;
    this.weaknesses = props.weaknesses;
  }

  get age() {
    return this.calcAge();
  }

  calcAge() {
    return this.deathDate - this.birthDate;
  }
}

// ...there was a guy named Vlad
const Dracula = new Vampire({
  location: "Transylvania",
  birthDate: 1428,
  deathDate: 1476,
  weaknesses: ["Sunlight", "Garlic"],
});

```

ooooooh js...


```python
# Once upon a time...

class Vampire:
  def __init__(self, props):
    self.location = props['location']
    self.birthDate = props['birthDate']
    self.deathDate = props['deathDate']
    self.weaknesses = props['weaknesses']

  def get_age(self):
    return self.calc_age()

  def calc_age(self):
    return self.deathDate - self.birthDate

# ...there was a guy named Vlad

Dracula = Vampire({
  'location': 'Transylvania',
  'birthDate': 1428,
  'deathDate': 1476,
  'weaknesses': ['Sunlight', 'Garlic']
})
```

k im bored lol.
