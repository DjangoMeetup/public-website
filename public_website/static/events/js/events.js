$(function(){
 var month = {
 	'1': 'Jan',
 	'2': 'Feb',
 	'3': 'Mar',
 	'4': 'Apr',
 	'5': 'May',
 	'6': 'Jun',
 	'7': 'Jul',
 	'8': 'Aug',
 	'9': 'Sep',
 	'10': 'Oct',
 	'11': 'Nov',
 	'12': 'Dec',

 };
 	$('.event_list-month').each(function(){
 		var month_name = month[$(this).text()];
 		$(this).text(month_name);
 	});
});