# HW2 - Requirements

## **1. Agile **

---

### Completed User Stories\*\*

#### User Story 1

As a vanilla git power-user that has never seen GiggleGit before, I want to quickly understand how to use the features it has so I can integrate it in my workflow..

- **Task:** Create interactive tutorial
  - **Ticket 1:** Design a guided onboarding tutorial for new users.
  - **Ticket 2:** Implement a tutorial help section in the UI.

#### User Story 2

As a team lead onboarding an experienced GiggleGit user, I want to create a easy to understand documentations and design a workflow so my entire team can use it efficiently.\_

- Task: Create clear documentation and design worflow dor using GiggleGit
  - Ticket 1: Write a GitHub Markdown user guide.
  - Ticket 2: Design a workflow for the team to integrate GiggleGit into their work.

#### User Story 3

As a developer who loves memes and Marvel, I want to customize GiggleGit’s meme selection for merge conflicts to show Marvel-related Memes, so I can have more fun while working.

- Task: Allow users to choose meme styles for merges
  - Ticket 1: Create a settings page for customizing meme selection.
  - Ticket 2: Implement an API for fetching memes selected by users from an external meme database.

---

### Not a User Story\*\*

_"As a user, I want to be able to authenticate on a new machine."_

#### Why isn’t this a user story?

- This is not a user story because it lacks a clear goal or motivation, this statement is more like a feature request or a high-level requirement.

---

## 2. Formal Requirements

### Non-Functional Requirements & Functional Requirements

#### List one goal and one non-goal

- Goal: Ensure SnickerSync provides an engaging Git diff experience using humor
- Non-Goal: Not intended to replace traditional Git diff tools but complement them.

#### Non-Functional Requirement 1: Access Control

_Only authorized users should have access to configure SnickerSync._

##### Functional Requirements:

1. Implement user authentication for SnickerSync settings.
2. Restrict meme configuration access to only repo admins.

#### Non-Functional Requirement 2: User Analytics

Gather analytics on user behavior and preferences for meme-based merge conflict resolution.

##### Functional Requirements:

1. Track user metrics based on their interactions with SnickerSync.
2. Assign participants into control and experimental groups for feature testing.

---
