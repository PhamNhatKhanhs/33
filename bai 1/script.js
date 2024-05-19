document.getElementById('fetchButton').addEventListener('click', function() {
    fetch('https://jsonplaceholder.typicode.com/users')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(users => {
            const display = document.getElementById('dataDisplay');
            display.innerHTML = '<ul>';
            // Thêm hàng tiêu đề
            display.innerHTML += `<li class="header"><span class="info">Tên</span><span class="info">Email</span><span class="info">Điện thoại</span><span class="info">Địa chỉ</span><span class="info">Công ty</span></li>`;
            users.forEach(user => {
                display.innerHTML += `<li class="user-row"><span class="info">${user.name}</span><span class="info">${user.email}</span><span class="info">${user.phone}</span><span class="info">${user.address.city}, ${user.address.street}</span><span class="info">${user.company.name}</span></li>`;
            });
            display.innerHTML += '</ul>';
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
    // Ẩn nút sau khi nhấp
    this.style.display = 'none';
});

