# README

Architecture: Microservices.

SOLID:
- SRP: Student only manages student logic.
- OCP: WaitlistedEnrollment extends Enrollment.
- DIP: Business logic depends on EnrollmentRepository.

Observer keeps Admin Panel loosely coupled to Email and Audit services.

Redundancy: Use primary-replica replication. On primary failure, promote a replica. Synchronous replication increases write latency but minimizes data loss. Recover missing transactions from WAL/binlog if needed.