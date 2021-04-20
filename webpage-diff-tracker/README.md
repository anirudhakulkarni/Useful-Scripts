## Why?

As course professor noted - "It is absolutely wasteful to send mail to everybody in the course. So all general and particular announcements, notices etc will be put up on the course homepage. So make sure you regularly visit the course homepage and check for updates." here is a small pain reducer. Host it on pythonanywhere or Wayscript

## What is this?

1. Timepass
2. When run stores visits pages stored in script.py and Hashes collected data with SHA224 hash function.
3. If previous hash is not available just stores the hash
4. Compares hash generated with previously stored hash in ./hashes directory.
5. If hash is different then corresponding emails will be sent according to data.json (configure it first)
6. Even single character will create entirely different hash so you wont miss small details on the page

## Usage:

1. Hashes stored in ./hashes.
2. Create a file by name data.json in root directory. Check data-sample.json for idea.

   ```Sample JSON file
   {
       "from-email":senderemailid,
       "to-email":recipientemailid,
       "from-password": password,
       "urls":["https://www.cse.iitd.ac.in/~sak/courses/pl/2020-21/index.html",
           "https://www.cse.iitd.ac.in/~sak/courses/pl/2020-21/header.html",
           "https://www.cse.iitd.ac.in/~sak/courses/pl/2020-21/timetable.html",
           "https://www.cse.iitd.ac.in/~sak/courses/pl/2020-21/PL-calendar.html",
           "https://www.cse.iitd.ac.in/~sak/courses/pl/2020-21/evaluation.html",
           "https://www.cse.iitd.ac.in/~sak/courses/pl/2020-21/caution.html",
           "https://www.cse.iitd.ac.in/~sak/courses/pl/2020-21/references.html",
           "https://www.cse.iitd.ac.in/~sak/courses/pl/2020-21/smlnj-references.html",
           "https://www.cse.iitd.ac.in/~sak/courses/pl/2020-21/prolog-references.html",
           "https://www.cse.iitd.ac.in/~sak/courses/pl/2020-21/exam-schedules.html"]
   }

   ```
3. Deploy it to some free hosting services like pythonanywhere or wayscript and schedule it as you wish.
4. Use wayscript.py to use on wayscript

## Notes:

1. This will fail if prof changes page structure. Don't relay too much on this
2. Use secondary email id as its not recommended to send email by this way. Visit [Less secure app access (google.com)](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OGE60EcjbsgvDG6ue34tyEQOkKYHbfycghgtemzUrgysQUScQ1KqESSYGIbVJlDvR_Xl-boWnTFoXMGYI_18vL361MxA) and turn it on for the account through which you wish to send mails.
