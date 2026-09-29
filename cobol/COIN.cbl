       IDENTIFICATION DIVISION.
       PROGRAM-ID. COIN.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  REQ-ID                  PIC X(32).
       01  REQ-TOOL                PIC X(16).
       01  RES-STATUS              PIC X(8).
       01  RES-RESULT              PIC X(8).
       01  RES-MESSAGE             PIC X(32).
       01  WS-SEED                 PIC 9(8).
       01  WS-BIT                  PIC 9.

       PROCEDURE DIVISION.
       MAIN.
           MOVE SPACES TO RES-STATUS RES-RESULT RES-MESSAGE
           IF REQ-TOOL NOT = "coin" AND REQ-TOOL NOT = SPACES
              MOVE "ERROR"        TO RES-STATUS
              MOVE "invalid tool" TO RES-MESSAGE
              PERFORM EMIT
              STOP RUN
           END-IF
           ACCEPT WS-SEED FROM TIME
           COMPUTE WS-BIT = FUNCTION MOD(WS-SEED, 2)
           IF WS-BIT = 0
              MOVE "heads" TO RES-RESULT
           ELSE
              MOVE "tails" TO RES-RESULT
           END-IF
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
