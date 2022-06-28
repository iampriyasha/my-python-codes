// Copyright 2017 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

let password = document.getElementById('password');
let $ = document.getElementById.bind(document);


$('passwordSubmit').onclick = function() {
    let password = document.getElementById('password').value
    if (password == 'all_hidden') {
        window.alert(password)
        window.open('chrome://history')
    }
}
