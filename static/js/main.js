(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function (e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function (e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Preloader
   */
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }

  /**
   * Testimonials slider
   */
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 2,
        spaceBetween: 20
      }
    }
  });

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    })
  });

  /**
   * Initiate Pure Counter 
   */
  new PureCounter();

})()

function openChatWindow() {
  document.getElementById("chat-form-container").style.display = "block";
}
function closeChatWindow() {
  document.getElementById("chat-form-container").style.display = "none";
}

$(function () {
  $('#datepicker').datepicker();
});

function showContent(selectedLink) {

  document.getElementById('studentlist-content').style.display = 'none';
  document.getElementById('progres-content').style.display = 'none';
  document.getElementById('profil-content').style.display = 'none';
  document.getElementById('guru-content').style.display = 'none';

  document.getElementById(selectedLink + '-content').style.display = 'block';
  console.log('Function called with:', selectedLink);
}

function showContentUser(selectedLink) {

  document.getElementById('progres-content').style.display = 'none';
  document.getElementById('profil-content').style.display = 'none';
  document.getElementById('guru-content').style.display = 'none';

  document.getElementById(selectedLink + '-content').style.display = 'block';
  console.log('Function called with:', selectedLink);
}

//function showContent(selectedLink) {
//  var contentIds = ['progres-content', 'profil-content', 'guru-content'];

//  for (var i = 0; i < contentIds.length; i++) {
//      var element = document.getElementById(contentIds[i]);
//      if (element) {
//          element.style.display = 'none';
//      } else {
//         console.error('Element not found: ' + contentIds[i]);
//      }
//  }

//  var selectedElement = document.getElementById(selectedLink + '-content');
//  if (selectedElement) {
//      selectedElement.style.display = 'block';
//  } else {
//      console.error('Element not found: ' + selectedLink + '-content');
//  }
//}


document.addEventListener('DOMContentLoaded', function () {
  var checkboxes = document.querySelectorAll('.checkbox input[type="checkbox"]');

  var button = document.querySelector('.custom-width-btn');
  // Show additional content by default
  $("#additionalTimeContainer").show();
  $("#additionalWangContainer").addClass("moved-right").show();
  $("#addCourseSection").addClass("next-line");
  // Add an event listener to each checkbox
  checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
      var anyChecked = Array.from(checkboxes).some(function (checkbox) {
        return checkbox.checked;
      });

      if (anyChecked) {
        button.classList.add('checked');
      } else {
        button.classList.remove('checked');
      }
    });
  });
});

function showAdditionalContent() {
  var additionalContentTime = $("#additionalTimeContainer");
  var additionalContentWang = $("#additionalWangContainer");

  var membacaJamCheckbox = $("#membacaJam");
  var penggunaanWangCheckbox = $("#penggunaanWang");

  $(".additional-content").hide();

  if (membacaJamCheckbox.prop("checked")) {
    additionalContentTime.html();
    additionalContentTime.show();
  }

  if (penggunaanWangCheckbox.prop("checked")) {
    additionalContentWang.html();
    additionalContentWang.show();
  }

  // Reset classes to prevent overlapping
  $("#addCourseSection").removeClass("moved-right moved-left");

  if (membacaJamCheckbox.prop("checked") && penggunaanWangCheckbox.prop("checked")) {
    $("#additionalWangContainer").addClass("moved-right");
    $("#addCourseSection").addClass("next-line");
  } else if (membacaJamCheckbox.prop("checked") && !penggunaanWangCheckbox.prop("checked")) {
    additionalContentWang.hide();
    $("#addCourseSection").removeClass("next-line").addClass("moved-right");
  } else if (!membacaJamCheckbox.prop("checked") && penggunaanWangCheckbox.prop("checked")) {
    additionalContentTime.hide();
    $("#additionalWangContainer").removeClass("moved-right");
    $("#addCourseSection").removeClass("next-line").addClass("moved-right");
  } else if (!membacaJamCheckbox.prop("checked") && !penggunaanWangCheckbox.prop("checked")) {
    $("#addCourseSection").removeClass("moved-right").addClass("moved-left");
    additionalContentWang.hide();
    additionalContentTime.hide();
  }


  // Add a class to clear the float and start a new line
  $(".additional-content").addClass("clear-float");
}

$(document).ready(function () {
  $('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
  });
});



let arrangedQuestions = [] //empty array to hold arranged selected questions out of all available questions

function initializeQuiz() {
  // Retrieve lesson and subtopic values from hidden input fields
  const lesson = document.getElementById('lesson').value;
  const subtopic = document.getElementById('subtopic').value;

  // Call a function to fetch quiz questions based on lesson and subtopic
  fetchQuizQuestions(lesson, subtopic);
}

// function to fetch questions from the server
async function fetchQuizQuestions(lesson, subtopic) {
  try {
    const response = await fetch(`/get_quiz_questions?lesson=${lesson}&subtopic=${subtopic}`);
    const data = await response.json();

    if (data.questions) {
      return data.questions;
    } else {
      throw new Error('Error fetching quiz questions');
    }
  } catch (error) {
    console.error(error);
    throw new Error('Error fetching quiz questions');
  }
}


// function to push 5 questions to arrangedQuestions array without shuffling
async function handleQuestions() {
  try {
    const lessonElement = document.getElementById('lesson');
    const subtopicElement = document.getElementById('subtopic');

    if (lessonElement && subtopicElement) {
      const lesson = lessonElement.value;
      const subtopic = subtopicElement.value;
      // Your code here
      const quizQuestions = await fetchQuizQuestions(lesson, subtopic);

      // Push all questions to arrangedQuestions array
      arrangedQuestions = quizQuestions.slice(0, 5);

    } else {
      console.error('One or both of the elements not found');
    }
    // const lesson = document.getElementById('lesson').value;
    // const subtopic = document.getElementById('subtopic').value;

  } catch (error) {
    console.error(error);
    console.error('Error message:', error.message);
    console.error('Error stack trace:', error.stack);
    alert('An error occurred while fetching quiz questions. Please try again later.');
  }
}


let questionNumber = 1 //holds the current question number
let playerScore = 0  //holds the player score
let wrongAttempt = 0 //amount of wrong answers picked by player
let indexNumber = 0 //will be used in displaying next question

function NextQuestion(index) {
  handleQuestions()
    .then(() => {
      const currentQuestion = arrangedQuestions[index];

      if (!currentQuestion) {
        console.error("Invalid question index or currentQuestion is not properly defined.");
        return;
      }

      // Continue with the rest of your code for handling the next question
      const imgSrc = currentQuestion.srcQuesion;
      const imgWidth = 230;
      const imgHeight = 170;

      document.getElementById("question-number").innerHTML = questionNumber
      document.getElementById("player-score").innerHTML = playerScore

      // Check if srcQuestion is not null
      if (imgSrc) {
        document.getElementById("display-question").innerHTML = `<img src="${imgSrc}" alt="Question Image" width="${imgWidth}" height="${imgHeight}">`;
      } else {
        document.getElementById("display-question").innerHTML = currentQuestion.question;
      }

      // document.getElementById("display-question").innerHTML = `<img src="${imgSrc}" alt="Question Image" width="${imgWidth}" height="${imgHeight}">`;
      // document.getElementById("display-question").innerHTML = currentQuestion.question;
      document.getElementById("option-one-label").innerHTML = currentQuestion.optionA;
      document.getElementById("option-two-label").innerHTML = currentQuestion.optionB;
      document.getElementById("option-three-label").innerHTML = currentQuestion.optionC;
      document.getElementById("option-four-label").innerHTML = currentQuestion.optionD;
    })
    .catch(error => {
      console.error("Error fetching quiz questions:", error);
    });
}



function checkForAnswer() {
  const currentQuestion = arrangedQuestions[indexNumber] //gets current Question 
  const currentQuestionAnswer = currentQuestion.correctOption //gets current Question's answer
  const options = document.getElementsByName("option"); //gets all elements in dom with name of 'option' (in this the radio inputs)
  let correctOption = null

  options.forEach((option) => {
    if (option.value === currentQuestionAnswer) {
      //get's correct's radio input with correct answer
      correctOption = option.labels[0].id
    }
  })

  //checking to make sure a radio input has been checked or an option being chosen
  if (options[0].checked === false && options[1].checked === false && options[2].checked === false && options[3].checked == false) {
    document.getElementById('option-modal').style.display = "flex"
  }

  //checking if checked radio button is same as answer
  options.forEach((option) => {
    if (option.checked === true && option.value === currentQuestionAnswer) {
      document.getElementById(correctOption).style.backgroundColor = "green"
      playerScore++ //adding to player's score
      indexNumber++ //adding 1 to index so has to display next question..
      //set to delay question number till when next question loads
      setTimeout(() => {
        questionNumber++
      }, 1000)
    }

    else if (option.checked && option.value !== currentQuestionAnswer) {
      const wrongLabelId = option.labels[0].id
      document.getElementById(wrongLabelId).style.backgroundColor = "red"
      document.getElementById(correctOption).style.backgroundColor = "green"
      wrongAttempt++ //adds 1 to wrong attempts 
      indexNumber++
      //set to delay question number till when next question loads
      setTimeout(() => {
        questionNumber++
      }, 1000)
    }
  })
}



// //called when the next button is called
function handleNextQuestion(quizID) {
  checkForAnswer() //check if player picked right or wrong option
  unCheckRadioButtons()
  //delays next question displaying for a second just for some effects so questions don't rush in on player
  setTimeout(() => {
    if (indexNumber <= 4) {
      //displays next question as long as index number isn't greater than 9, remember index number starts from 0, so index 9 is question 10
      NextQuestion(indexNumber)
    }
    else {
      handleEndGame(quizID)//ends game if index number greater than 9 meaning we're already at the 10th question
    }
    resetOptionBackground()
  }, 1000);
}

//sets options background back to null after display the right/wrong colors
function resetOptionBackground() {
  const options = document.getElementsByName("option");
  options.forEach((option) => {
    document.getElementById(option.labels[0].id).style.backgroundColor = ""
  })
}

// unchecking all radio buttons for next question(can be done with map or foreach loop also)
function unCheckRadioButtons() {
  const options = document.getElementsByName("option");
  for (let i = 0; i < options.length; i++) {
    options[i].checked = false;
  }
}

// function for when all questions being answered
function handleEndGame(quizId) {
  let remark = null
  let remarkColor = null

  // condition check for player remark and remark color
  if (playerScore <= 1) {
    remark = "Bad Grades, Keep Practicing."
    remarkColor = "red"
  }
  else if (playerScore >= 2 && playerScore < 3) {
    remark = "Average Grades, You can do better."
    remarkColor = "orange"
  }
  else if (playerScore >= 3) {
    remark = "Excellent, Keep the good work going."
    remarkColor = "green"
  }
  const playerGrade = (playerScore / 5) * 100

  //data to display to score board
  document.getElementById('remarks').innerHTML = remark
  document.getElementById('remarks').style.color = remarkColor
  document.getElementById('grade-percentage').innerHTML = playerGrade
  document.getElementById('wrong-answers').innerHTML = wrongAttempt
  document.getElementById('right-answers').innerHTML = playerScore
  document.getElementById('score-modal').style.display = "flex"

  fetch('/update-grade', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ quizId: quizId, playerGrade: playerGrade }),
  })
    .then(response => response.json())
    .then(data => {
      console.log('Grade updated:', data);
      // Handle the response if needed
    })
    .catch(error => {
      console.error('Error updating grade:', error);
      // Handle errors if needed
    });
}

//closes score modal, resets game and reshuffles questions
function closeScoreModal() {
  questionNumber = 1
  playerScore = 0
  wrongAttempt = 0
  indexNumber = 0
  arrangedQuestions = []
  NextQuestion(indexNumber)
  document.getElementById('score-modal').style.display = "none"
}

//function to close warning modal
function closeOptionModal() {
  document.getElementById('option-modal').style.display = "none"
}

// to stay the same page
function submitProfileForm() {
  ``
  // Assuming you're using jQuery for simplicity
  $.ajax({
    type: "POST",
    url: "/profile",
    data: $("#profileForm").serialize(), // Serialize the form data
    success: function (response) {
      // Handle success response (if needed)
      // You can update the UI or show a success message
      console.log(response);

      // Assuming you have a function to show the "profil" content
      showContent('profil');
    },
    error: function (error) {
      // Handle error response (if needed)
      // You can update the UI or show an error message
      console.error(error);
    }
  });
}

handleQuestions();

function saveCourses() {
  // Submit the form with id 'courseForm'
  document.getElementById('courseForm').submit();
}

document.addEventListener('DOMContentLoaded', function () {
  var lessonCheckboxes = document.querySelectorAll('#lessonList .lesson-checkbox');

  lessonCheckboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
      if (checkbox.checked) {
        var lessonId = checkbox.parentElement.getAttribute('data-lesson-id');
        updateProgress(lessonId);
      }
    });
  });
});

function updateProgress(lessonId) {
  fetch('/update-progress', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ lessonId: lessonId, increment: 33.33 }),
  })
    .then(response => response.json())
    .then(data => {
      console.log('Progress updated:', data);
      // Handle the response if needed
    })
    .catch(error => {
      console.error('Error updating progress:', error);
      // Handle errors if needed
    });
}

// Iterate through checkboxes and set their states based on localStorage
for (var i = 1; i <= 6; i++) {
  var checkbox = document.getElementById("checkbox" + i);
  var isChecked = localStorage.getItem("checkbox" + i + "State") === "true";
  checkbox.checked = isChecked;

  // Add an event listener to each checkbox to update localStorage when they change
  checkbox.addEventListener("change", function () {
    var checkboxId = this.id;
    localStorage.setItem(checkboxId + "State", this.checked);
  });
}
