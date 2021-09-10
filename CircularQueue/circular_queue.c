#include <stdio.h>
#include <stdlib.h>

typedef struct {
  void **values;
  size_t size;
  size_t front;
  size_t rear;
} CircularQueue;

CircularQueue create_queue(size_t size) {
  void **mem = malloc(sizeof(void *) * size);
  return (CircularQueue){mem, size, 0, 0};
}

int append(CircularQueue queue, void *element) {
  if (queue.rear == queue.size) {
    // full
    return -1;
  }

  queue.values[queue.rear] = element;
  queue.rear = (queue.rear + 1) % queue.size;
  return 0;
}

void *pop(CircularQueue queue) {
  void *elem = queue.values[queue.front];
  queue.values[queue.front] = NULL;
  queue.front = (queue.front + 1) % queue.size;
  return elem;
}

int main(void) {
  CircularQueue q = create_queue(10);
  append(q, "hello");
  char *value = (char *)pop(q);
  printf("%s\n", value);
  free(q.values);
  return 0;
}
