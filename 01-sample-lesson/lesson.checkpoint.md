# Sample Snippet tests

Testing snippet

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: custom-snippet
* language: sql
* id: 98fbaecb-ed84-473a-8b61-d89531e323f1
* title: Creating a table
* docker_directory_path: /custom-snippets/test-create-table
* points: 1
* topics: sql

##### !question

* Create a drivers table with the following fields:
  * full_name - VARCHAR(32)
  * id  - PRIMARY KEY INT (auto-incremented)
  * VIN - VARCHAR(32)
##### !end-question

##### !placeholder

```
CREATE ...
```

##### !end-placeholder

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->