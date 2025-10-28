function delete_card(self) {
  var task = $(self).data("task-id");
  var card = self.closest(".card");
  $.ajax({
    type: "GET",
    url: "/task_delete/",
    data: {
      task_to_delete: task,
    },
    success: function () {
      card.remove();
    },
    error: function () {
      alert("Failed");
    },
  });
}