class Event {
  constructor(event) {
    this.eventId = event.data("event");
    this.userId = event.data("user");
    this.subscribeBtn = event.find(".update-event");
    this.withdrawBtn = event.find(".withdraw_btn");
    this.subscribeBtn.on("click", this.handelSubscribe);
    this.withdrawBtn.on("click", this.handelWithdraw);
  }

  handelSubscribe = () => {
    this.AddParticipant(this.eventId);
  };
  handelWithdraw = () => {
    this.withdrawEvent(this.eventId, this.userId);
  };

  withdrawEvent = (eventId, userId) => {
    let url = `/api/my_events/${userId}`;
    let successUrl = "/";
    updateApi(url, eventId, successUrl);
  };
  AddParticipant = (eventId) => {
    let url = `/api/events/${eventId}`;
    let successUrl = "users/subscribed_events/";
    updateApi(url, null, successUrl);
  };
}

$(".event").each(function () {
  let newEvent = new Event($(this));
});
