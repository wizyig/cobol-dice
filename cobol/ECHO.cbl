       IDENTIFICATION DIVISION.
       PROGRAM-ID. ECHO.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  REQ-ID                  PIC X(32).
       01  REQ-TOOL                PIC X(16).
       01  REQ-PAYLOAD             PIC X(80).
       01  WS-LEN                  PIC 9(4) VALUE 0.
       01  WS-I                    PIC 9(4).
       01  WS-CH                   PIC X.
       01  RES-STATUS              PIC X(8).
       01  RES-RESULT              PIC X(80).
       01  RES-MESSAGE             PIC X(32).

       PROCEDURE DIVISION.
       MAIN.
           MOVE SPACES TO RES-STATUS RES-RESULT RES-MESSAGE
           IF REQ-TOOL NOT = "echo" AND REQ-TOOL NOT = SPACES
              MOVE "ERROR"        TO RES-STATUS
              MOVE "invalid tool" TO RES-MESSAGE
              PERFORM EMIT
              STOP RUN
           END-IF
           IF REQ-PAYLOAD = SPACES
              MOVE "ERROR"           TO RES-STATUS
              MOVE "invalid payload" TO RES-MESSAGE
              PERFORM EMIT
              STOP RUN
           END-IF
           PERFORM VARYING WS-I FROM 80 BY -1 UNTIL WS-I < 1
              IF REQ-PAYLOAD(WS-I:1) NOT = SPACE
                 MOVE WS-I TO WS-LEN
                 MOVE 1 TO WS-I
              END-IF
           END-PERFORM
           IF WS-LEN = 0
              MOVE "ERROR"           TO RES-STATUS
              MOVE "invalid payload" TO RES-MESSAGE
              PERFORM EMIT
              STOP RUN
           END-IF
           MOVE REQ-PAYLOAD TO RES-RESULT
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
