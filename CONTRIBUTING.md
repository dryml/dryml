# Contribution Guide

DRYML project accepts contributions via git pull requests. Each pull request shall be raised against the specific GitHub [Issue(-s)](https://github.com/dryml/dryml/issues) (see below for more information).
This document outlines some of the conventions on submission workflow, commit message formatting, contact points, and other resources to make it easier to get your contribution done and accepted.



## What to contribute

There are several ways of how one can contribute to the DRYML Project:

* Documentation
* Code
* Tests



All the items, which require contribution, are tracked as [Issues](https://github.com/dryml/dryml/issues). Look for the "good first issue" tag in order not to lose yourself in plenty of items.

To understand better, what the project is created for and hot it's supposed to work, it's strongly recommended to start from the [Documentation](./DOCUMENTATION). The documentation is organized corresponding to the Software Artefact, identified in the [AIFORSE Information Framework - Data Model Map - Level 0](https://medium.com/ai-for-software-engineering/software-engineering-artifacts-lets-agree-on-terminology-4f009b351361).



### Contributing to Documentation

1. Review the [Documentation Management Methodology](https://medium.com/ai-for-software-engineering/software-engineering-artifacts-lets-agree-on-terminology-4f009b351361)
2. Review [actual DRYML Documentation](./DOCUMENTATION)
3. Review open documentation [Issues](https://github.com/dryml/dryml/issues)
4. Requirements for specific Artefact Types
   1. **Business Journey**
      1. Shall have a reference to at least one Business Goal by its ID
   2. **Business Case**
      1. Shall have a reference to at least one Business Journey by its ID
   3. **Business Requirement**
      1. Shall have a reference to at least one Business Case by its ID
      2. Shall have Acceptance Criteria defined in the way of at least one User Story
   4. **Use Case**
      1. Shall have a reference to at least one Business Case by its ID
   5. **Functional Requirement**
      1. Shall be created as an Issue with the FR (Functional Requirement) tag
      2. Shall have a reference to at least one Use Case by its ID
      3. Shall have Acceptance Criteria defined in the way of at least one Gherkin Test
5. Fork repository, make changes, create signed commit, create a pull request, mention which issue you're resolving



### Contributing to Code

1. Review the [Documentation Management Methodology](https://medium.com/ai-for-software-engineering/software-engineering-artifacts-lets-agree-on-terminology-4f009b351361)
2. Review [actual DRYML Documentation](./DOCUMENTATION)
3. Review open FR (Functional Requirement) [Issues](https://github.com/dryml/dryml/issues)
4. Code Requirements
   1. Solution shall be provided in Python 3
   2. Before making a commit, run [Black Formatter](https://black.readthedocs.io/en/stable/)
   3. Software Architecture shall follow the [DDD](https://en.wikipedia.org/wiki/Domain-driven_design) principles, specifically implement the approach, defined in the article "[What is the Level of your Tech Start-up? Part 1/3. Software Technical Architecture](https://medium.com/ai-for-software-engineering/what-is-the-level-of-your-tech-start-up-part-1-3-software-architecture-df24d4db1b19)"
   4. Each Solution, provided or updated in the PR, shall be covered with passing test(s), provided in the same PR, implementing Acceptance Criteria, provided in the selected FR (Functional Requirement) Issue
5. Fork repository, make changes, create signed commit, create a pull request, mention which issue you're resolving



### Contributing to Test

1. Review the [Documentation Management Methodology](https://medium.com/ai-for-software-engineering/software-engineering-artifacts-lets-agree-on-terminology-4f009b351361)
2. Review [actual DRYML Documentation](./DOCUMENTATION)
3. Then, two modes are available:
   1. Create/ update [Test Cases](./TEST%20CASES)
      1. Test Cases Requirements
         1. Shall have a reference to at least one Documentation Artefact being tested by its ID
         2. Shall have pre-condition(s), execution step(s), and expected result(s)
         3. Fork repository, make changes, create signed commit, create a pull request, mention which issue you're resolving
   2. Execute Test(s)
      1. Create a new Issue with the 'defect' tag
         1. Shall have a reference to at least one Artefact being tested by its ID/ reference
         2. Shall have pre-condition(s), execution step(s), expected result(s), and achieved result(s)



## How to contribute

Pull Requests are the main way to contribute.
All the PRs have to pass the personal evaluation of the Project Administrator.

### Format of the Commit Message

The commit summary must start with "Added"/"Updated"/"Removed" and end with a dot.



## Contributor License Agreement

By contributing to DRYML you agree to the [DRYML Individual Contributor License Agreement (DICLA)](DRYML%20Individual%20Contributor%20License%20Agreement.md). 

In order to show your agreement with the DICLA, you should include at the end of a commit message
the following line: `Signed-off-by: John Doe <john.doe@example.com>`, using your real name.

This can be done using the [`-s`](https://git-scm.com/docs/git-commit) flag on the `git commit`.



## Support Channels

The official support channels, for both users and contributors, are:

- GitHub [Issues](https://github.com/dryml/dryml/issues)*

**Before opening a new issue or submitting a new pull request, it's helpful to search the project - it's likely that another user has already reported the issue you're facing, or it's a known issue that we're already aware of.*



## Propose a Feature

* Open an [issue](https://github.com/dryml/dryml/issues) with a detailed description of your proposed feature, the motivation for it and alternatives considered. Please note we may close this issue or ask you to create a pull-request if this is not something we see as a sufficiently high priority.