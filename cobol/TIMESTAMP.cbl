       IDENTIFICATION DIVISION.
       PROGRAM-ID. TIMESTAMP.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  REQ-ID                  PIC X(32).
       01  REQ-TOOL                PIC X(16).
       01  RES-STATUS              PIC X(8).
       01  RES-RESULT              PIC X(16).
       01  RES-MESSAGE             PIC X(32).
       01  WS-DATE                 PIC 9(8).
       01  WS-TIME                 PIC 9(8).

       PROCEDURE DIVISION.
       MAIN.
           MOVE SPACES TO RES-STATUS RES-RESULT RES-MESSAGE
           IF REQ-TOOL NOT = "timestamp" AND REQ-TOOL NOT = SPACES
              MOVE "ERROR"        TO RES-STATUS
              MOVE "invalid tool" TO RES-MESSAGE
              PERFORM EMIT
              STOP RUN
           END-IF
           ACCEPT WS-DATE FROM DATE YYYYMMDD
           ACCEPT WS-TIME FROM TIME
           STRING WS-DATE DELIMITED BY SIZE
                  "T"     DELIMITED BY SIZE
                  WS-TIME DELIMITED BY SIZE
                  INTO RES-RESULT
           MOVE "OK" TO RES-STATUS
           PERFORM EMIT
           STOP RUN.

       EMIT.
           DISPLAY "{"
           DISPLAY "  ""request_id"": """ REQ-ID """"
           DISPLAY "  ,""status"": """ RES-STATUS """"
           IF RES-STATUS = "OK"
              DISPLAY "  ,""result"": """ RES-RESULT """"
           ELSE
              DISPLAY "  ,""message"": """ RES-MESSAGE """"
           END-IF
           DISPLAY "}"
           .
