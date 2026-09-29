       IDENTIFICATION DIVISION.
       PROGRAM-ID. DICE.

      * COBOL Dice v0.1
      * Knows: request / response records only.
      * Does not know: MCP, AI, LLM, Agent.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       COPY REQUEST.
       COPY RESPONSE.

       01  WS-SEED                 PIC 9(8).
       01  WS-MOD                  PIC 9(4).

       PROCEDURE DIVISION.
       MAIN.
           PERFORM INIT-RESPONSE
           PERFORM VALIDATE
           IF RES-STATUS = "ERROR"
              PERFORM EMIT
              STOP RUN
           END-IF
           PERFORM ROLL
           PERFORM EMIT
           STOP RUN.

       INIT-RESPONSE.
           MOVE REQ-ID TO RES-ID
           MOVE SPACES TO RES-STATUS
           MOVE ZERO   TO RES-RESULT
           MOVE SPACES TO RES-MESSAGE.

       VALIDATE.
           IF REQ-TOOL NOT = "dice"
              MOVE "ERROR"         TO RES-STATUS
              MOVE "invalid tool"  TO RES-MESSAGE
              EXIT PARAGRAPH
           END-IF
           IF REQ-SIDES < 2 OR REQ-SIDES > 1000
              MOVE "ERROR"          TO RES-STATUS
              MOVE "invalid sides"  TO RES-MESSAGE
              EXIT PARAGRAPH
           END-IF
           MOVE "OK" TO RES-STATUS.

       ROLL.
           ACCEPT WS-SEED FROM TIME
           COMPUTE WS-MOD = FUNCTION MOD(WS-SEED, REQ-SIDES)
           COMPUTE RES-RESULT = WS-MOD + 1
           MOVE SPACES TO RES-MESSAGE.

       EMIT.
           DISPLAY "{"
           DISPLAY "  ""request_id"": """ RES-ID """"
           DISPLAY "  ,""status"": """ RES-STATUS """"
           IF RES-STATUS = "OK"
              DISPLAY "  ,""result"": " RES-RESULT
           ELSE
              DISPLAY "  ,""message"": """ RES-MESSAGE """"
           END-IF
           DISPLAY "}"
           .
