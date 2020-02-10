# DRYML -- compiled software modelling language, for free


## About DRYML

**DRYML** (an acronym for “**DRY Modelling Language**”) is both a human- and machine-readable software modelling language.

**DRY** (an acronym for “**Don’t repeat yourself**”) is a principle of software development aimed at reducing repetition of software patterns, replacing it with abstractions or using data normalization to avoid redundancy. *[*[*Wikipedia*](https://en.wikipedia.org/wiki/Don't_repeat_yourself)*]*

**Here how it looks like:**

```
james->mary: love
    in:
        flowers [fresh]
            colour = red
        chocolate [solid]
            type = milk
    out:
        kisses
            sweet = true
        hugs
            strong = true
```

For the basic information about the DRYML, read the article "[**Introducing DRYML**](https://medium.com/@v.grigoryevskiy/introducing-dryml-7d9e049ac91)"



## Main Principles and Reasoning

Two core (set of) principles were used during the development of the DRYML

1. **Software Models Data shall be linked/ integrated** -- in order to solve the following tasks
   1. **Ensure Software Model Data Consistency** - when you create several diagrams in PlantUML of Visio, they are completely detached; so if the same object described in two places needs to be changed, you need to do this twice, and no data consistency is validated
   2. **Manage Software Model Knowledge** by querying it, finding relationships and dependencies
   3. **Compile Software Model** - find out about Model Decrepancies before implementing it
   4. **Test Software Model** - find Model Defects before implementing it
   5. **Reduce Time and Costs** of turning Software Model into the working Solution - provide a baseline for code autogeneration
2. **Software Models Data shall conform to the AIFORSE [Information Framework Principles](https://gitlab.com/aiforse/aiforse-framework/-/blob/master/Information%20Framework%20(AIFORSE_infoF)/Information%20Framework%20Principles.md)**
3. **DRYML shall be just one of the possible implementations** -- the external standard, defined in the [AIFORSE Integration Framework](https://gitlab.com/aiforse/aiforse-framework/-/blob/master/Integration%20Framework%20(AIFORSE_intgF)/AIFORSE%20Integration%20Framework.md),  [Process JSON Schema](https://gitlab.com/aiforse/aiforse-framework/-/blob/master/Integration%20Framework%20(AIFORSE_intgF)/Schemas/aiforse-integration-framework---process-json-schema.json), creates the perfect condition for development and competition of similar tools
4. **Eased adoption** -- integrate with the notations and tools engineers are used to (UML, PlantUML, IntelliJ IDEA), in order to, first, make the adoption process as smooth as possible, and second, benefit and provide additional value to users from such integrations



## Documentation

The documentation structure follows the recommendation, defined in the "[AIFORSE Information Framework](https://gitlab.com/aiforse/aiforse-framework/-/blob/master/Information%20Framework%20(AIFORSE_infoF)/AIFORSE%20Information%20Framework.md)", which are explained in the article "[Software Engineering Artifacts — Let’s agree on Terminology](https://medium.com/ai-for-software-engineering/software-engineering-artifacts-lets-agree-on-terminology-4f009b351361)".

* [Solution Description](./DOCUMENTATION/Solution%20Description/)
  * [Solution Architecture](./DOCUMENTATION/Solution%20Description/Solution%20Architecture/)



## Contribution Guide

Read the [Contribution Guide](./CONTRIBUTING.md).



## License

DRYML is licensed under the [GNU General Public License v3.0](./LICENSE).
