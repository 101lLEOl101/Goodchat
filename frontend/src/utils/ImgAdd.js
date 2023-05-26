export const addImageCodeFragment = `
						function removeFilesItem(target){
							document.getElementById("img-name").innerHTML = "NoneImg";
							let input = $(target).closest('.input-file-row').find('input[type=file]');
							$(target).closest('.input-file-list-item').remove();
							input[0].files = (new DataTransfer()).files;
							document.getElementById('add_btn').removeAttribute("style");
							document.getElementById("box-img").removeAttribute("style");
							document.getElementById("input-list").removeAttribute("style");
						}
                        `