const hourItems = document.querySelectorAll(`.hour`);
const hourBox = document.querySelector(`.hourly-weather`);
const logoBtn = document.querySelector(`.logo`);
const listCity = document.querySelector(`.list-city`);

const obsSettings = {
  root: hourBox,
  threshold: 0,
};

const fadeIn = function (e) {
  const [event] = e;
  if (event.isIntersecting) {
    event.target.style.marginTop = `0`;
  }
};
let observer = new IntersectionObserver(fadeIn, obsSettings);
hourItems.forEach((el) => observer.observe(el));
logoBtn.addEventListener(`click`, function (e) {
  listCity.classList.toggle(`show`);
});