# Test Summary
System was tested by sending UART commands.
3 defects were found:
- System declines PWM value 100 (major)
- RESET command doesn't reset led and pwm values (blocker)
- Command GET TEMP returns malformed json (critical)

Also, it was found that command PING is performed longer than other commands. But there're no requirements about specific timeout for command so framework was updated for this timeout.

No suggested moving build to release until fixing defects with critical, major  and blocker severity.
