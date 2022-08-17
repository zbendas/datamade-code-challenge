/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
'use strict'

const submitButton = document.getElementById('submit')
const resultsContainer = document.getElementById('address-results')
const resultsTableBody = resultsContainer.querySelector('table tbody')
const addressInput = document.getElementById('address')

const invalidFeedback = document.createElement('div')
addressInput.insertAdjacentElement('afterend', invalidFeedback).classList.add('invalid-feedback')

submitButton.addEventListener('click', (event) => {
  event.preventDefault()
  const address = addressInput.value
  resultsTableBody.innerHTML = null
  addressInput.classList.remove('is-invalid')
  fetch(`api/parse/?address=${address}`)
    .then(async response => {
      const data = response.headers.get('content-type').includes('application/json') ? await response.json() : null

      if (!response.ok) {
        const error = (data && data.error) || response.status
        return Promise.reject(error)
      } else {
        return Promise.resolve(data)
      }
    })
    .then(data => {
      document.getElementById('parse-type').innerText = data['address_type']
      Object.entries(data['address_components']).map(([tag, addressPart]) => {
        const newRow = document.createElement('tr')
        const newPartCell = document.createElement('td')
        newPartCell.innerText = addressPart
        const newTagCell = document.createElement('td')
        newTagCell.innerText = tag
        newRow.append(newPartCell, newTagCell)
        resultsTableBody.append(newRow)
      })
      resultsContainer.style.removeProperty('display')
    })
    .catch(error => {
      addressInput.classList.add('is-invalid')
      invalidFeedback.innerText = error
      resultsContainer.style.display = 'none'
    })
})
