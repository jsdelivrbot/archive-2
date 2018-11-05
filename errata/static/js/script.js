  $('div.accordion').accordion({collapsible: true,
                                active: false,
                                heightStyle: "content",
                               });

  $('div.nested-accordion').accordion({collapsible: true,
                                       active: false,
                                       heightStyle: 'content',
                                       beforeActivate: function(event, ui) {
                                                         if (ui.newHeader[0]) {
                                                           var myAccordion = $(event.target);
                                                           var myPageHeader = $(event.currentTarget);
                                                           var myChapterHeader = myPageHeader.parent().prev();

                                                           var myPageNumber = myPageHeader.text().match(/(\d+)/)[0];
                                                           var myChapterNumber = myChapterHeader.text().match(/(\d+)/)[0];
                                                         
                                                           myPageHeader.next().find('img').attr('src', 'static/img/' + myChapterNumber + '/' + myPageNumber + '.jpg');
                                                         }
                                                       }
                                       });
