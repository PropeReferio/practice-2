// // JOI practice
const Joi = require('@hapi/joi');

const schema = Joi.object().keys({
  // username: Joi.string().alphanum().min(3).max(30).required(),
  // password: Joi.string().regex(/^[a-zA-Z0-9]{3,30}$/),
  creditCardNumber: Joi.string().creditCard().required(),
  name: Joi.string().min(2).max(26).required(),
  expireDate: Joi.string().regex(/^(0[1-9]|1[0-2])\/?([0-9]{4}|[0-9]{2})$/).required(),
  CCV: Joi.number().integer().min(-1).max(10000).required(),
})

response = schema.validate({ 
  creditCardNumber: '372329801792006',
  name: 'Lemuel Stevens',
  expireDate: '06/23',
  CCV: 0026
});

if (response.error) {
  console.log('There is an error')
  console.log(response.error)
} else {
  console.log('Data valid')
}


// const Joi = require('@hapi/joi') 
  
//User-defined function to validate the user 
// function validateUser(user) 
// { 
//     const JoiSchema = Joi.object({ 
//         username: Joi.string().min(5).max(30).required(), 
//         email: Joi.string().email().min(5).max(50).optional(),  
//         date_of_birth: Joi.date().optional(),  
//         account_status: Joi.string().valid('activated') 
//                       .valid('unactivated').optional(), 
//     }).options({ abortEarly: false }); 
  
//     return JoiSchema.validate(user) 
// } 
  
// var user = { 
//     username: 'Gourav', 
//     email: 'gourav@gmail.com', 
//     date_of_birth: '2020-8-11', 
//     account_status: 'activated'
// } 
  
// response = validateUser(user)
// console.log(response) 
  
// if(response.error) 
// {   
//     console.log(response.error.details) 
// } 
// else
// { 
//     console.log("Validated Data") 
// } 
