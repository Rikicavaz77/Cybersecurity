window.onscroll = function() {
  scroll() };

function scroll() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("go-to-top").classList.add("active");
  } else {
    document.getElementById("go-to-top").classList.remove("active");
  }
}

function menuOC() {
  var menu = document.getElementById("menu");
  var hamb = document.getElementById("hamburger");
  var footer = document.getElementById("footer");
  
  if (!menu.classList.contains('active')) {
    menu.classList.add('active');
    hamb.classList.add('close');
    footer.classList.add('above');
    document.body.classList.add('remove-scroll');
  } else {
    menu.classList.remove('active');
    hamb.classList.remove('close');
    footer.classList.remove('above');
    document.body.classList.remove('remove-scroll');
  }
}

async function getFilesFromRepo(url) {
  try {
    const response = await fetch(url);
    const files = await response.json();

    if (response.ok) {
      return files;
    } else {
      console.error('Errore nel recupero dei file: ', files);
      return [];
    }
  } catch (error) {
    console.error(error);
    return [];
  }
}

async function getFileContent(fileUrl) {
  const response = await fetch(fileUrl);
  if (response.ok) {
    const fileContent = await response.text();
    return fileContent;
  } else {
    return 'Impossibile caricare il file: ' + fileUrl;
  }
}

async function generateFileList(folderUrl) {
  const files = await getFilesFromRepo(folderUrl);
  const listElement = document.createElement('ul');
  listElement.classList.add('file-list');

  for (const file of files) {
    const li = document.createElement('li');

    if (file.type === 'file') {
      const fileLink = document.createElement('a');
      fileLink.href = "#file-content";
      fileLink.textContent = file.name;
      fileLink.onclick = async function () {
        const fileContent = await getFileContent(file.download_url);
        const fileContentBox = document.getElementById('file-content');
        fileContentBox.prepend(fileContent);
        fileContentBox.classList.remove('hidden'); 
      };

      li.appendChild(fileLink);
    } else if (file.type === 'dir') {
      const folderLink = document.createElement('a');
      folderLink.href = "#";
      folderLink.textContent = file.name;
      folderLink.onclick = async function(event) {
        event.preventDefault();
        const existingSubList = li.querySelector('ul');
        if (existingSubList) {
          existingSubList.style.display = existingSubList.style.display === 'none' ? 'block' : 'none';
        } else {
          const folderPath = file.url;
          const subList = await generateFileList(folderPath);
          li.appendChild(subList);
        }
      };

      li.appendChild(folderLink);
    }

    listElement.appendChild(li);
  }

  return listElement;
}

async function loadFolders() {
  let folderURL = 'https://api.github.com/repos/Rikicavaz77/Cybersecurity/contents/Crypto/';
  let folderElement = document.getElementById('crypto').querySelector('.folders');
  let fileList = await generateFileList(folderURL);
  folderElement.appendChild(fileList);
  folderURL = 'https://api.github.com/repos/Rikicavaz77/Cybersecurity/contents/ReverseEngineering/';
  folderElement = document.getElementById('reveng').querySelector('.folders');
  fileList = await generateFileList(folderURL);
  folderElement.appendChild(fileList);
  folderURL = 'https://api.github.com/repos/Rikicavaz77/Cybersecurity/contents/Web/';
  folderElement = document.getElementById('web').querySelector('.folders');
  fileList = await generateFileList(folderURL);
  folderElement.appendChild(fileList);
}

loadFolders();

function toggleCopyIcon() {
  document.getElementById('copy-to-clipboard').querySelector('i').classList.toggle('fa-copy');
  document.getElementById('copy-to-clipboard').querySelector('i').classList.toggle('fa-check');
}

document.getElementById('copy-to-clipboard').addEventListener('click', () => {
  const fileContent = document.getElementById('file-content').textContent;
  toggleCopyIcon();
  navigator.clipboard.writeText(fileContent.trim()).then(() => {
    setTimeout(() => {
      toggleCopyIcon();
    }, 1000);
  }).catch(err => {
    console.error('Errore durante la copia: ', err);
    toggleCopyIcon();
  });
});