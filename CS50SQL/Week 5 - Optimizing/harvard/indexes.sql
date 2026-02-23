CREATE INDEX "enrollments_index" ON "enrollments" ("student_id");
CREATE INDEX "enrollments_index_2" ON "enrollments" ("course_id");
CREATE INDEX "courses_index" ON "courses" ("title", "department", "number", "semester");
CREATE INDEX "satisfies_index" ON "satisfies" ("course_id", "requirement_id");
