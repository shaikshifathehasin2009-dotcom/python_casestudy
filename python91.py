## 1. Advanced String-Based Registration Record Analyzer

### Algorithm

1. Start.
2. Input the registration records as structured strings.
3. Split each string into individual fields.
4. Validate the field lengths and formats.
5. If any field is invalid, classify and record the error.
6. Extract the specified components from valid fields.
7. Check whether duplicate registration records exist.
8. Classify errors as length errors, format errors, missing-field errors, or duplicate errors.
9. Display the extracted components, duplicate records, and error classifications.
10. Stop.

### Flowchart

START

INPUT

Registration strings

PARSE RECORDS

Split strings into fields

VALIDATE FIELDS

Check length and format

Are fields valid?

NO

Classify errors

Length / Format / Missing field

YES

Extract specified components

CHECK DUPLICATES

Compare registration records

GENERATE REPORT

Extracted data and error classifications

STOP

### Input

- Registration records in string format.
- Required field lengths and formats.
- Components to be extracted.
- Existing records for duplicate checking.

Example input: `REG101,Ali,ali@gmail.com,2026`

### Output

- Extracted registration ID, name, email, and year.
- Valid and invalid record details.
- Duplicate registration records, if any.
- Error classifications: length error, format error, missing-field error, and duplicate error.